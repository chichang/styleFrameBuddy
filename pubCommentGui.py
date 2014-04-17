# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/USERS/chichang/tools/mari/styleFrameBuddy/media/pubCommentGui.ui'
#
# Created: Tue Apr 15 18:37:16 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!


from PythonQt import QtCore, QtGui

class Ui_pubCommentGUI(QtGui.QDialog):

    def __init__(self):
        super(Ui_pubCommentGUI, self).__init__()

    def setupUi(self):

        #set Main Window Title.
        self.setWindowTitle("Mari Publish")

        self.setObjectName("pubCommentGUI")
        self.setEnabled(True)
        self.resize(330, 282)
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
        self.commentTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.mid_HBoxLayout.addWidget(self.commentTextEdit)
        self.gridLayout_2.addLayout(self.mid_HBoxLayout, 3, 0, 1, 1)
        self.top_GridLayout = QtGui.QGridLayout()
        self.top_GridLayout.setObjectName("top_GridLayout")
        self.showTitleLable = QtGui.QLabel(self.centralwidget)
        self.showTitleLable.setObjectName("showTitleLable")
        self.top_GridLayout.addWidget(self.showTitleLable, 1, 0, 1, 1)
        self.showLable = QtGui.QLabel(self.centralwidget)
        self.showLable.setObjectName("showLable")
        self.top_GridLayout.addWidget(self.showLable, 1, 1, 1, 1)
        self.assetLable = QtGui.QLabel(self.centralwidget)
        self.assetLable.setObjectName("assetLable")
        self.top_GridLayout.addWidget(self.assetLable, 3, 1, 1, 1)
        self.assetTitleLable = QtGui.QLabel(self.centralwidget)
        self.assetTitleLable.setObjectName("assetTitleLable")
        self.top_GridLayout.addWidget(self.assetTitleLable, 3, 0, 1, 1)
        self.shotTitleLable = QtGui.QLabel(self.centralwidget)
        self.shotTitleLable.setObjectName("shotTitleLable")
        self.top_GridLayout.addWidget(self.shotTitleLable, 2, 0, 1, 1)
        self.shotLable = QtGui.QLabel(self.centralwidget)
        self.shotLable.setObjectName("shotLable")
        self.top_GridLayout.addWidget(self.shotLable, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.top_GridLayout, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.commentLable = QtGui.QLabel(self.centralwidget)
        self.commentLable.setObjectName("commentLable")
        self.gridLayout_2.addWidget(self.commentLable, 2, 0, 1, 1)
        self.bottom_VBoxLayout = QtGui.QVBoxLayout()
        self.bottom_VBoxLayout.setObjectName("bottom_VBoxLayout")
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
        self.gridLayout_2.addLayout(self.bottom_VBoxLayout, 4, 0, 1, 1)


        self.setLayout(self.gridLayout_2)


        self.showTitleLable.setText("   Show  :")
        self.shotTitleLable.setText("   Shot  :")
        self.assetTitleLable.setText("  Asset :")
        setBold(self.showTitleLable)
        setBold(self.shotTitleLable)
        setBold(self.assetTitleLable)


        self.cancel_Button.setText("Cancel")
        self.publishButton.setText("Publish")
        self.commentLable.setText("Comment")
        self.publishButton.setStyleSheet("QPushButton{background-color: rgb(150, 200, 150); color: rgb(50,50,50)}")


    def retranslateUi(self, pubCommentGUI):
        pubCommentGUI.setWindowTitle(QtGui.QApplication.translate("pubCommentGUI", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.showTitleLable.setText(QtGui.QApplication.translate("pubCommentGUI", "Show :", None, QtGui.QApplication.UnicodeUTF8))
        self.showLable.setText(QtGui.QApplication.translate("pubCommentGUI", "show", None, QtGui.QApplication.UnicodeUTF8))
        self.assetLable.setText(QtGui.QApplication.translate("pubCommentGUI", "styleframes", None, QtGui.QApplication.UnicodeUTF8))
        self.assetTitleLable.setText(QtGui.QApplication.translate("pubCommentGUI", "Asset :", None, QtGui.QApplication.UnicodeUTF8))
        self.shotTitleLable.setText(QtGui.QApplication.translate("pubCommentGUI", "Shot :", None, QtGui.QApplication.UnicodeUTF8))
        self.shotLable.setText(QtGui.QApplication.translate("pubCommentGUI", "shot", None, QtGui.QApplication.UnicodeUTF8))
        self.commentLable.setText(QtGui.QApplication.translate("pubCommentGUI", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_Button.setText(QtGui.QApplication.translate("pubCommentGUI", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.publishButton.setText(QtGui.QApplication.translate("pubCommentGUI", "Publish", None, QtGui.QApplication.UnicodeUTF8))


def setBold(widget):
    font = widget.font
    font.setWeight(75)
    widget.setFont(font)