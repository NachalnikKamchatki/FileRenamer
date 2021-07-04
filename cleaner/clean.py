# -*- coding: utf-8 -*-
# cleaner/clean.py

"""This module provides the Cleaner class to clean info multiple files."""

import time
from pathlib import Path
import os
# from docx import Document


from PyQt5.QtCore import QObject, pyqtSignal
import exif


class Cleaner(QObject):

    # Define custom signals
    progressed = pyqtSignal(int)
    cleanedFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files):
        super().__init__()
        self._files = files

    def cleanMSDocMetadata(name):
        if os.path.exists(name):
            doc = Document(name)

            coreprops.author           = '1'
            coreprops.comments         = '1'
            coreprops.identifier       = '1'
            coreprops.subject          = '1'
            coreprops.title            = '1'

            doc.save(name)
            status = f'{name} metadata succesfully cleared'
        else:
            status = f'File {name} not exist'
        print(status)

    def clearFilesInfo(self):
        for fileNumber, file in enumerate(self._files, 1):
            # if file.endswith('.docx'):
            #     cleanMSDocMetadata(name=file)
            #     continue

            try:
                exif_image = exif.Image(file)
            except:
                status = 'Format not supported'
                exif_image = None

            if exif_image and exif_image.has_exif:
                # print(dir(exif_image))
                exif_image.delete_all()

                with open(file, 'wb') as upd_file:
                    upd_file.write(exif_image.get_file())

                status = 'exif data succesfully cleared'

            else:
                status = "does not contain any EXIF information."

            print(f"Image {file} {status}")
            time.sleep(0.02)
            self.progressed.emit(fileNumber)
            self.cleanedFile.emit(file)
        self.progressed.emit(0)
        self.finished.emit()
