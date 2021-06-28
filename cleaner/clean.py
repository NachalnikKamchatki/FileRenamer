# -*- coding: utf-8 -*-
# cleaner/clean.py

"""This module provides the Cleaner class to clean info multiple files."""

import time
from pathlib import Path


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

    def clearFilesInfo(self):
        for fileNumber, file in enumerate(self._files, 1):
            exif_image = exif.Image(file)
            if exif_image.has_exif:
                print(dir(exif_image))
                # exif_image.delete_all()
                # status = 'exif data succesfully cleared'

                # with open(file, 'wb') as upd_file:
                #     upd_file.write(exif_image.get_file())

                # status = f"""

                # ----------------------------

                # Device Information - Image {fileNumber}
                # Make: {exif_image.get('make', 'unknown')}
                # Model: {exif_image.get('model', 'unknown')}

                # ---------------------

                # Lens and OS
                # Lens make: {exif_image.get('lens_make', 'Unknown')}
                # Lens model: {exif_image.get('lens_model', 'Unknown')}
                # Lens specification: {exif_image.get('lens_specification', 'Unknown')}
                # OS version: {exif_image.get('software', 'Unknown')}

                # ---------------------

                # Date/time taken
                # {exif_image.get('datetime_original', 'unknown')}.{exif_image.get('subsec_time_original', 'unknown')} {exif_image.get('offset_time', '')}

                # ---------------------

                # Coordinates
                # Latitude: {exif_image.get('gps_latitude', 'unknown')} {exif_image.get('gps_latitude_ref', 'unknown')}
                # Longitude: {exif_image.get('gps_longitude', 'unknown')} {exif_image.get('gps_longitude_ref', 'unknown')}"""
            else:
                status = "does not contain any EXIF information."

            print(f"Image {fileNumber} {status}")
            time.sleep(0.02)
            self.progressed.emit(fileNumber)
            self.cleanedFile.emit(file)
        self.progressed.emit(0)
        self.finished.emit()
