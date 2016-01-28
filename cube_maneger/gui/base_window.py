#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from functools import partial
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import gui_abs as gui
import manager_window
from cube_maneger.libs import plugin


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

    def add_games(self):
        self.adapter_plugin = plugin.AdapterPluginsGame(
                "game_plugin", 'game', "GamePlugin")
        mod_objects = self.adapter_plugin.plugin_objects(
                self.adapter_plugin.paths)
        for game_widget in mod_objects:
            object_name = game_widget.name
            index = game_widget.index
            button_name = game_widget.tool_btn_name
            home_btn = game_widget.home_btn

            self.plugin_valid(index, button_name, object_name)

            home_btn.clicked.connect(self.return_to_global_window)
            self.stack.insertWidget(index, game_widget)

            button = self.global_game_window.create_game_button(
                button_name, index)
            button.clicked.connect(partial(self.press_game, index))

    def plugin_valid(self, *atr):
        for i in atr:
            if i is None:
                raise Exception("ERROR - {} not None".format(i))

    @QtCore.pyqtSlot(int)
    def press_game(self, s):
        pass
        self.stack.setCurrentIndex(s)

    def return_to_global_window(self):
        self.stack.setCurrentIndex(0)


if __name__ == '__main__':
    pass
    # app = QtWidgets.QApplication(sys.argv)
    # # app.setStyleSheet(open('./css/{0}.css'.format('base'), "r").read())
    # app.setStyleSheet(open('../css/base.css').read())
    # main = Main()
    # main.show()
    # sys.exit(app.exec_())
