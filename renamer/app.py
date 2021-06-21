# -*- coding: utf-8 -*-
# renamer/app.py

"""This module provides the FilesRenamer application."""


import sys

from PyQt5.QtWidgets import QApplication

from .views import Window


def main():
    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec())
