#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

import gui_abs as gui
import manager_window


class Main(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.cfg = config["base"]


        self.center = gui.Frame("center_frame", self)
        self.setCentralWidget(self.center)

        self.stack = gui.StackedLayout()
        box = gui.Box(gui.Box._horizontal, self.center)
        box.addLayout(self.stack)

        self.global_game_window = manager_window.MangerWindow(
                "manager_window", self, config["global_game_window"],
                self.center,
        )
        self.stack.add_widget(self.global_game_window)

    def register_control(self, control_object, slot, *args):
        control_object.clicked.connect(getattr(self, slot))

    @QtCore.pyqtSlot()
    def exit(self):
        sys.exit()

if __name__ == '__main__':
    pass
    # app = QtWidgets.QApplication(sys.argv)
    # # app.setStyleSheet(open('./css/{0}.css'.format('base'), "r").read())
    # app.setStyleSheet(open('../css/base.css').read())
    # main = Main()
    # main.show()
    # sys.exit(app.exec_())
