
#======================
# Mari Style Frame Buddy
#======================
import os
import sys
sys.path.append("/USERS/chichang/tools/mari/styleFrameBuddy/")
import json
import re
import mari
from PythonQt import QtCore, QtGui
import xgUtils as imp_utils
reload(imp_utils)
import styleFrameBuddyGui
reload(styleFrameBuddyGui)
import pubCommentGui
reload(pubCommentGui)
import publish
reload(publish)

#======================================================================
#	UTIL
#======================================================================
debug = 0
mu = imp_utils.ccMariUtil()
su = imp_utils.ccSysUtil(os.getenv("SHOW"), os.getenv("SHOT"))
formats = [".tif", ".tiff", ".png", ".exr", ".jpeg", ".jpg"]
saveFormat = ".tif"
tempName = "mariStyleframeTemp"

#======================================================================
#   WINDOW
#======================================================================

def debugMsg(message):
    if debug == 1:
        print message

class styleFrameBuddyWindow():
    '''
    the main gui class.
    '''
    #===========================#
    NEW_VER = "v001"
    #===========================#

    def __init__(self):

        # Check that we're starting from a state where exporting channels is possible
        if not mu.isProjectSuitable():
            return

        #set up ui
        self.gui = QtGui
        self.ui = styleFrameBuddyGui.Ui_styleFrameBuddyGUI()
        self.ui.setupUi()

        #geral info from mari
        userAssetDir = os.getenv("USER_SHOT_DIR")
        self.styleFramePath = os.path.join(userAssetDir,"images","elements","styleframes")
        self.currentMariAsset = mari.projects.current().name()
        self.currentObj = mari.geo.current().name()


        #set ui title
        self.show = os.environ.get("SHOW", None)
        self.shot = os.environ.get("SHOT", None)
        self.tempPath = os.environ.get("TEMP", None)
        self.ui.setWindowTitle("Style Frame Buddy"+" | "+self.shot)

        #check if there is an existing version for the texture type
        latestVer = su.getNewVersion(self.styleFramePath, self.currentMariAsset)

        if not latestVer:
            newVersion = self.NEW_VER
        else:
            newVersion = latestVer

        #fill inital ui info
        self.ui.savePathLineEdit.setText(self.styleFramePath + "/" + self.currentMariAsset + "/" + newVersion)


        #connect callbacks
        self.ui.browseButton.connect("clicked()", self.browseForFolder)
        self.ui.cancel_Button.connect("clicked()", self.ui.reject)
        self.ui.renderButton.connect("clicked()", self.render)
        self.ui.publishButton.connect("clicked()", self.publish)
        self.ui.savePathLineEdit.connect("textChanged(QString)", self.savePathUpdate)
        self.ui.savePathLineEdit.connect("textEdited(QString)", self.savePathUpdate)
        self.ui.styleFramesList.connect("itemDoubleClicked(QListWidgetItem *)", self.showImage)


        #set export chan list to empty
        self.savePath = self.ui.savePathLineEdit.text
        self.styleframes=[]

    def showUI(self):
        '''
        show gui.
        '''
        if not mu.isProjectSuitable():
            return
    	#show ui.
        self.ui.show()


    def browseForFolder(self):
        '''
        browser for choosing the output dir. 
        '''
        #Get Folder
        defaultDir = self.ui.savePathLineEdit.text
        fileDialog = self.gui.QFileDialog(0,"Select Directory for Export")
        fileDialog.setDirectory(defaultDir)
        dirname = fileDialog.getExistingDirectory()
        if dirname:
            self.ui.savePathLineEdit.setText(dirname)
            self.savePath = self.ui.savePathLineEdit.text


    def savePathUpdate(self):
        '''
        clear the table widget when export path is updated.
        '''
        # reset display and remove any existing rows
        self.ui.styleFramesList.clear()
        self.styleframes=su.listFiles(self.ui.savePathLineEdit.text)

        if len(self.styleframes) != 0:
            print self.ui.savePathLineEdit.text
            #print self.styleframes
            self.styleframes.sort()
            for image in self.styleframes:
                if os.path.splitext(image)[-1] in formats:
                    self.ui.styleFramesList.addItem(image)

        else:
            print "no styleframes found."


    def render(self):

        saveDir = self.ui.savePathLineEdit.text
        if saveDir == "" :
            mu.messageBox("Please select an output directory.")
            return

        #print "render."
        self.step = 0

        #create projector
        self.createProjector()
        print "render cam: " + self.activeProjector.name() + " ..."


        self.updateProgressBar()
        #check if the export path is not in the SHOT directory.
        #create root folder if doesnt exist
        if not os.path.exists(saveDir):
            try:
                os.makedirs(saveDir)
                print "Directory created: ", saveDir

            except OSError:
                mu.messageBox("Error creating directory: '%s'" % saveDir)
                #errors.append("Error creating directory: '%s'" % saveDir)
                #return errors
                self.ui.reject()
                return

        #unproject
        self.updateProgressBar()

        #fileName = self.currentMariAsset + "_" + self.currentObj
        fileName = self.shot + "_" + self.currentMariAsset

        savePath = self.ui.savePathLineEdit.text

        nextName = self.getName(os.listdir(savePath), fileName)
        print "file name up: " + nextName + " ..."

        unprojectPath = os.path.join(savePath, nextName)
        print "rendering file: " + unprojectPath

        if os.path.exists(unprojectPath):
            mu.messageBox("File exist: '%s'" % unprojectPath)
            self.ui.reject()
            return

        #Render
        self.updateProgressBar()
        self.activeProjector.unprojectToFile(unprojectPath)

        self.updateProgressBar()
        #remove projector
        print "removing render cam ..."
        mari.projectors.remove(self.activeProjector.name())

        self.updateProgressBar()
        #set camera back to Ortho
        mari.actions.find("/Mari/Canvas/Camera/Ortho Camera").trigger()

        self.updateProgressBar()

        #image comping
        backgroundImagePath = self.makeBackground(self.renderResolution)
        if backgroundImagePath:
            #oiiotool _default_Head_example.0002.tif --over gray_4096.tif -o gbacktest.tif
            try:
                callString = "oiiotool " + unprojectPath + " --over " + backgroundImagePath + " -o " + unprojectPath
                print "calling ", callString
                su.runCommand(callString)

            except:
                print "error compositing image."
                pass

        else:
            print "can not get background image!"


        #updating list
        self.ui.progressBar.setValue(100)
        self.ui.progressBar.reset()

        #updating list
        self.savePathUpdate()


    def publish(self):
        #print "publish."

        publishFrames = self.styleframes
        if len(publishFrames) == 0:
            mu.messageBox("Nothing to publish ...")
            return

        print "publishing frames: " + str(publishFrames)

        publisher = publish.SimplePublisher()

        pubCommentGUI = PubCommentWindow(self.show, self.shot)
        #modal
        pubCommentGUI.ui.exec_()


        if pubCommentGUI.ui.result():

            print "ready to publish ..."

            comment = pubCommentGUI.ui.commentTextEdit.plainText

            print "publish comment:\n" + "==========================="
            print comment
            print "==========================="

            publishPath = self.ui.savePathLineEdit.text
            #info for publish
            pubInfo = dict()

            pubInfo["SHOW"] = self.show
            pubInfo["SHOT"] = self.shot
            pubInfo["ASSET"] = pubCommentGUI.ui.assetLable.text
            pubInfo["PATH"] = publishPath
            pubInfo["USER"] = os.getenv('USER') or os.getenv('USERNAME')
            pubInfo["QUIET"] = True
            pubInfo["COMMENT"] = comment
            pubInfo["publishMode"] = 1  # 0 (move), 1 (copy), 2 (symlink)

            print "publishing styleframes in: " + publishPath

            print "pub Info: "
            print json.dumps(pubInfo, sort_keys=True, indent=4)



            result = publisher.publishStyleframes(publishPath, pubInfo)

            if not result:
                mu.messageBox("Publish failed ! \nPlease check console for more detail.")
            
            else:
                #success
                infoStr = pubInfo["ASSET"]+" Published. \nPlease check console for more detail.\n\n"
                infoStr += "------------------------\n"
                infoStr += "the following was submitted to published:\n"
                for i in self.styleframes:
                    infoStr += i + "\n"

                mu.messageBox(infoStr)
                self.ui.reject()

        else:
            print "publish canceled."



    def showImage(self):
        selected_chan = [item.text() for item in self.ui.styleFramesList.selectedItems()]
        imagePath = os.path.join(self.savePath, selected_chan[0])
        cammandStr = "gwenview " + imagePath
        su.runCommand(cammandStr)


    def createProjector(self):

        self.updateProgressBar()

        print "creating projector ..."
        action = mari.actions.find("/Mari/Canvas/Projection/Create Projector")
        action.trigger()

        self.updateProgressBar()

        self.activeProjector = mari.projectors.current()

        if self.activeProjector is None: 
            print "Error Creating Projector."
            return 

        comboBoxIndex = self.ui.resolution_ComboBox.currentIndex
        self.renderResolution = self.imageResolution(comboBoxIndex)

        self.updateProgressBar()
        #setup projector
        self.activeProjector.setSize( self.renderResolution, self.renderResolution) 
        self.activeProjector.setFormat("RGBA")
        self.activeProjector.setPaintingMode("Normal")
        self.activeProjector.setLightingMode(self.activeProjector.FULL)
        self.activeProjector.setClampColors(True) 
        self.activeProjector.setUseShader("Current Shader")


    def getName(self, filesExist, fileName):
        """
        get next name.
        """
        #currentImages = glob.glob("*.jpg")
        numList = [0]
        for img in filesExist:
            print img
            i = os.path.splitext(img)[0]
            try:
                num = re.findall('[0-9]+$', i)[0]
                numList.append(int(num))
            except IndexError:
                pass
        numList = sorted(numList)
        newNum = numList[-1]+1
        saveName = fileName + '.%04d.tif' % newNum
        print "Saving %s" % saveName

        return saveName

    def thumbSave(self):
        canvas = mari.canvases.current()
        image = canvas.captureImage(scaled_width=0, scaled_height=0)
        image.save(image)


    def updateProgressBar(self):
        stepSize = 100/8
        self.step += stepSize
        self.ui.progressBar.setValue(self.step)

    def makeBackground(self, size, val = 128):

        #create background image
        backgroundImgName = tempName + "_" + str(size) + "_" + str(val) + saveFormat

        backgroundSavePath = os.path.join(self.tempPath, backgroundImgName)

        #check if file exist
        if os.path.exists(backgroundSavePath):
            print "found temp background."

        else:
            print "creating temp background:", backgroundSavePath
            image = QtGui.QPixmap(size, size)
            backColor = QtGui.QColor(val,val,val)
            image.fill(backColor)
            try:
                image.save(backgroundSavePath)
            except:
                print "error saving temp background."
                return None

        return backgroundSavePath


    def imageResolution(self, index):

        if index == 0:
            return 16384
        if index == 1:
            return 8192
        if index == 2:
            return 4096
        if index == 3:
            return 2048
        if index == 4:
            return 1024

#======================================================================
#   GUI
#======================================================================

class PubCommentWindow():

    def __init__(self, show, shot, asset="styleframes"):

        #set up ui
        self.ui = QtGui
        self.ui = pubCommentGui.Ui_pubCommentGUI()
        self.ui.setupUi()

        #set labels
        self.ui.showLable.setText(show)
        self.ui.shotLable.setText(shot)
        self.ui.assetLable.setText(asset)

        #connect callbacks
        self.ui.cancel_Button.connect("clicked()", self.ui.reject)
        self.ui.publishButton.connect("clicked()", self.publish)


    def publish(self):
        #check to see if comment is empty
        comment = self.ui.commentTextEdit.plainText

        if comment == "":
            mu.messageBox("Please enter comment.")
            return

        elif len(comment) < 10:
            mu.messageBox("Comment too short.")
            return

        #accept
        self.ui.accept()



#======================================================================
#   RUN
#======================================================================
if __name__ == "__main__":

    try:
        if styleFrameBuddy.ui.isVisible():
            styleFrameBuddy.ui.reject()
    except:
        pass

    styleFrameBuddy = styleFrameBuddyWindow()
	styleFrameBuddy.showUI()
