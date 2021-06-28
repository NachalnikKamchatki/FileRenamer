# -*- coding: utf-8 -*-
# renamer/views.py

"""This module provides the FilesRenamer main window."""

from collections import deque
from pathlib import Path
from renamer.rename import Renamer
from cleaner.clean import Cleaner


from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import QThread

from .ui.window import Ui_Window

from config import FILTERS


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._files = deque()
        self._files_count = len(self._files)
        self._setupUi()
        self._connectSignalsSlots()

    def _setupUi(self):
        self.setupUi(self)
        self._updateStateWhenNoFiles()

    def _connectSignalsSlots(self):
        self.loadFilesButton.clicked.connect(self.loadFiles)
        self.clearInfoButton.clicked.connect(self.clearFilesInfo)
        self.renameFilesButton.clicked.connect(self.renameFiles)
        self.prefixEdit.textChanged.connect(self._updateStateWhenReady)

    def _updateStateWhenReady(self):
        if self.prefixEdit.text():
            self.renameFilesButton.setEnabled(True)
            self.clearInfoButton.setEnabled(True)
        else:
            self.renameFilesButton.setEnabled(False)
            self.clearInfoButton.setEnabled(True)

    def loadFiles(self):
        self.dstFileList.clear()
        if self.dirEdit.text():
            initDir = self.dirEdit.text()
        else:
            initDir = str(Path.home())
        files, filter = QFileDialog.getOpenFileNames(
            self,
            "Choose Files to Rename",
            initDir,
            filter=FILTERS)

        if len(files) > 0:
            fileExtension = filter[filter.index("*"):-1]
            self.extensionLabel.setText(fileExtension)
            srcDirName = str(Path(files[0]).parent)
            self.dirEdit.setText(srcDirName)
            for file in files:
                self._files.append(Path(file))
                self.srcFileList.addItem(file)
            self._files_count = len(self._files)
            self._updateStateWhenFilesLoaded()

    def clearFilesInfo(self):
        self._runCleanerThread()
        self._updateStateWhileProcessing()

    def _updateStateWhenFilesLoaded(self):
        self.prefixEdit.setEnabled(True)
        self.prefixEdit.setFocus(True)
        self.clearInfoButton.setEnabled(True)

    def renameFiles(self):
        self._runRenamerThread()
        self._updateStateWhileProcessing()

    def _updateStateWhileProcessing(self):
        self.loadFilesButton.setEnabled(False)
        self.renameFilesButton.setEnabled(False)
        self.clearInfoButton.setEnabled(False)

    def _runRenamerThread(self):
        prefix = self.prefixEdit.text()
        self._thread = QThread()
        self._renamer = Renamer(
            files=tuple(self._files),
            prefix=prefix
        )
        self._renamer.moveToThread(self._thread)
        # Rename
        self._thread.started.connect(self._renamer.renameFiles)
        # Update state
        self._renamer.renamedFile.connect(self._updateStateWhenFileProcessed)
        self._renamer.progressed.connect(self._updateProgressBar)
        self._renamer.finished.connect(self._updateStateWhenNoFiles)
        # CleanUp
        self._renamer.finished.connect(self._thread.quit)
        self._renamer.finished.connect(self._renamer.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # Run the thread
        self._thread.start()

    def _runCleanerThread(self):
        self._thread = QThread()
        self._cleaner = Cleaner(
            files=tuple(self._files)
        )
        self._cleaner.moveToThread(self._thread)
        # Clean
        self._thread.started.connect(self._cleaner.clearFilesInfo)
        # Update state
        self._cleaner.cleanedFile.connect(self._updateStateWhenFileProcessed)
        self._cleaner.progressed.connect(self._updateProgressBar)
        self._cleaner.finished.connect(self._updateStateWhenNoFiles)
        # CleanUp
        self._cleaner.finished.connect(self._thread.quit)
        self._cleaner.finished.connect(self._cleaner.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # Run the thread
        self._thread.start()

    def _updateStateWhenFileProcessed(self, newFile):
        self._files.popleft()
        self.srcFileList.takeItem(0)
        self.dstFileList.addItem(str(newFile))

    def _updateProgressBar(self, fileNumber):
        progressPercent = int(fileNumber / self._files_count * 100)
        self.progressBar.setValue(progressPercent)

    def _updateStateWhenNoFiles(self):
        self._files_count = len(self._files)
        self.loadFilesButton.setEnabled(True)
        self.loadFilesButton.setFocus(True)
        self.renameFilesButton.setEnabled(False)
        self.clearInfoButton.setEnabled(False)
        self.prefixEdit.clear()
        self.prefixEdit.setEnabled(False)
