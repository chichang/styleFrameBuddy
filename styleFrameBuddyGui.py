# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/USERS/chichang/tools/mari/styleFrameBuddy/media/styleFrameBuddyGui.ui'
#
# Created: Fri Apr 11 18:57:17 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!


from PythonQt import QtCore, QtGui

class Ui_styleFrameBuddyGUI(QtGui.QDialog):

    def __init__(self):
        super(Ui_styleFrameBuddyGUI, self).__init__()

    def setupUi(self):
        #set Main Window Title.
        self.setWindowTitle("Style Frame Buddy")
        #self.setObjectName("xgTextureExportGUI")
        self.setObjectName("styleFrameBuddyGUI")
        self.setEnabled(True)
        self.resize(360, 528)
        self.centralwidget = QtGui.QWidget()
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        #self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mid_HBoxLayout = QtGui.QHBoxLayout()
        self.mid_HBoxLayout.setObjectName("mid_HBoxLayout")
        self.midLeft_GridLayout = QtGui.QGridLayout()
        self.midLeft_GridLayout.setObjectName("midLeft_GridLayout")
        self.styleFramesList = QtGui.QListWidget(self.centralwidget)
        self.styleFramesList.setObjectName("styleFramesList")
        self.midLeft_GridLayout.addWidget(self.styleFramesList, 0, 0, 1, 1)
        self.mid_HBoxLayout.addLayout(self.midLeft_GridLayout)
        self.gridLayout_2.addLayout(self.mid_HBoxLayout, 2, 0, 1, 1)
        self.bottom_VBoxLayout = QtGui.QVBoxLayout()
        self.bottom_VBoxLayout.setObjectName("bottom_VBoxLayout")
        self.renderButton = QtGui.QPushButton(self.centralwidget)
        self.renderButton.setMinimumSize(QtCore.QSize(0, 50))
        self.renderButton.setStyleSheet("QPushButton{background-color: rgb(200, 120, 20);}")
        self.renderButton.setObjectName("renderButton")
        self.bottom_VBoxLayout.addWidget(self.renderButton)
        self.exportButton_HBoxLayout = QtGui.QHBoxLayout()
        self.exportButton_HBoxLayout.setObjectName("exportButton_HBoxLayout")
        self.cancel_Button = QtGui.QPushButton(self.centralwidget)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.cancel_Button.sizePolicy().hasHeightForWidth())
        #self.cancel_Button.setSizePolicy(sizePolicy)
        self.cancel_Button.setMinimumSize(QtCore.QSize(0, 45))
        self.cancel_Button.setObjectName("cancel_Button")
        self.exportButton_HBoxLayout.addWidget(self.cancel_Button)
        self.publishButton = QtGui.QPushButton(self.centralwidget)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.publishButton.sizePolicy().hasHeightForWidth())
        #self.publishButton.setSizePolicy(sizePolicy)
        self.publishButton.setMinimumSize(QtCore.QSize(0, 45))
        self.publishButton.setStyleSheet("QPushButton{background-color: rgb(150, 200, 150);}")
        self.publishButton.setObjectName("publishButton")
        self.exportButton_HBoxLayout.addWidget(self.publishButton)
        self.bottom_VBoxLayout.addLayout(self.exportButton_HBoxLayout)
        self.gridLayout_2.addLayout(self.bottom_VBoxLayout, 3, 0, 1, 1)
        self.top_GridLayout = QtGui.QGridLayout()
        self.top_GridLayout.setObjectName("top_GridLayout")
        self.savePathLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.savePathLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.savePathLineEdit.setObjectName("savePathLineEdit")
        self.top_GridLayout.addWidget(self.savePathLineEdit, 1, 0, 1, 1)
        self.browseButton = QtGui.QPushButton(self.centralwidget)
        self.browseButton.setMinimumSize(QtCore.QSize(0, 30))
        self.browseButton.setStyleSheet("QPushButton{background-color: rgb(150, 200, 150);}")
        self.browseButton.setObjectName("browseButton")
        self.top_GridLayout.addWidget(self.browseButton, 1, 1, 1, 2)
        self.styleFrameLable = QtGui.QLabel(self.centralwidget)
        self.styleFrameLable.setObjectName("styleFrameLable")
        self.top_GridLayout.addWidget(self.styleFrameLable, 2, 0, 1, 1)
        self.resolution_Lable = QtGui.QLabel(self.centralwidget)
        self.resolution_Lable.setObjectName("resolution_Lable")
        self.top_GridLayout.addWidget(self.resolution_Lable, 2, 1, 1, 1)
        self.resolution_ComboBox = QtGui.QComboBox(self.centralwidget)
        self.resolution_ComboBox.setObjectName("resolution_ComboBox")
        self.top_GridLayout.addWidget(self.resolution_ComboBox, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.top_GridLayout, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        #self.progressBar.setProperty("value", 0)
        self.progressBar.reset()
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 1)
        #styleFrameBuddyGUI.setCentralWidget(self.centralwidget)
        #QtCore.QMetaObject.connectSlotsByName(styleFrameBuddyGUI)
        self.setLayout(self.gridLayout_2)









        self.renderButton.setText("Render")
        self.cancel_Button.setText("Cancel")
        self.publishButton.setText("Publish Styleframes")
        self.browseButton.setToolTip("Choose styleframe output directory.")
        self.browseButton.setText("Browse")
        self.styleFrameLable.setText("Style frames")
        self.resolution_Lable.setText("Resolution:")
        self.browseButton.setStyleSheet("QPushButton{background-color: rgb(150, 200, 150); color: rgb(50,50,50)}")
        self.publishButton.setStyleSheet("QPushButton{background-color: rgb(150, 200, 150); color: rgb(50,50,50)}")
        self.renderButton.setStyleSheet("QPushButton{background-color: rgb(200, 120, 20); color: rgb(50,50,50)}")

        self.resolution_ComboBox.addItem("16384 (16K)")
        self.resolution_ComboBox.addItem("8192 (8K)")
        self.resolution_ComboBox.addItem("4096 (4K)")
        self.resolution_ComboBox.addItem("2048 (2K)")
        self.resolution_ComboBox.addItem("1024 (1K)")

        self.resolution_ComboBox.setCurrentIndex(2)

        self.styleFramesList.setSelectionMode(self.styleFramesList.ExtendedSelection)






    def retranslateUi(self):
        styleFrameBuddyGUI.setWindowTitle(QtGui.QApplication.translate("styleFrameBuddyGUI", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.renderButton.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_Button.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.publishButton.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Publish Styleframes", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setToolTip(QtGui.QApplication.translate("styleFrameBuddyGUI", "Choose texture output directory.", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.styleFrameLable.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Style frames", None, QtGui.QApplication.UnicodeUTF8))
        self.resolution_Lable.setText(QtGui.QApplication.translate("styleFrameBuddyGUI", "Version ", None, QtGui.QApplication.UnicodeUTF8))

