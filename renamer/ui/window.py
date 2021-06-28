# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(640, 480)
        Window.setMinimumSize(QtCore.QSize(640, 480))
        Window.setMaximumSize(QtCore.QSize(1920, 1080))
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(Window)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prefixEdit = QtWidgets.QLineEdit(Window)
        self.prefixEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.prefixEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.prefixEdit.setObjectName("prefixEdit")
        self.horizontalLayout_2.addWidget(self.prefixEdit)
        self.extensionLabel = QtWidgets.QLabel(Window)
        self.extensionLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.extensionLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.extensionLabel.setObjectName("extensionLabel")
        self.horizontalLayout_2.addWidget(self.extensionLabel)
        self.renameFilesButton = QtWidgets.QPushButton(Window)
        self.renameFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameFilesButton.setObjectName("renameFilesButton")
        self.horizontalLayout_2.addWidget(self.renameFilesButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Window)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dirEdit = QtWidgets.QLineEdit(Window)
        self.dirEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout.addWidget(self.dirEdit)
        self.loadFilesButton = QtWidgets.QPushButton(Window)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.horizontalLayout.addWidget(self.loadFilesButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Window)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(self.layoutWidget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout.addWidget(self.srcFileList)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(self.layoutWidget1)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout_2.addWidget(self.dstFileList)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.clearInfoButton = QtWidgets.QPushButton(Window)
        self.clearInfoButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearInfoButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.clearInfoButton.setObjectName("clearInfoButton")
        self.horizontalLayout_3.addWidget(self.clearInfoButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "FilesRenamer"))
        self.label_4.setText(_translate("Window", "Filename prefix:"))
        self.extensionLabel.setText(_translate("Window", "*.jpg"))
        self.renameFilesButton.setText(_translate("Window", "&Rename"))
        self.label.setText(_translate("Window", "Last Source Directory:"))
        self.loadFilesButton.setText(_translate("Window", "Load Files"))
        self.label_2.setText(_translate("Window", "Files to rename:"))
        self.label_3.setText(_translate("Window", "Renamed:"))
        self.clearInfoButton.setText(_translate("Window", "Clear Info"))
