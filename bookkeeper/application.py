#!/home/int33h/.pyenv/shims/python3.10
"""
Графическое приложение.
"""

import sys
import os

if __name__ == "__main__" and __package__ is None:
    # main dir
    path = sys.path[0]
    index = path.index("bookkeeper") + len("bookkeeper")
    path = path[:index]

    # package
    __package__ = os.path.relpath(sys.path[0], path).replace('\\', '.')

    # sys.path modification (add main dir)
    sys.path.insert(1, path)

from PySide6.QtWidgets import QApplication
from bookkeeper.presenter import Bookkeeper
from bookkeeper.view.pyqt6_view import PyQtView
from bookkeeper.repository.sqlite_repository import SQLiteRepository


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = PyQtView()
    bookkeeper = Bookkeeper(view, SQLiteRepository)
    app.exec()
