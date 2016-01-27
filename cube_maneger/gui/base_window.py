#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets

import gui_abs as gui
import manager_window




class Main(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.center = gui.Frame("center_frame", self)
        self.setCentralWidget(self.center)

        self.stack = gui.StackedLayout()
        box = gui.Box(gui.Box._horizontal, self.center)
        box.addLayout(self.stack)

        # self.global_game_window = manager_window.GlobalMenu(
        #         "global_menu", parent=self,
        #         visual_parent=self.center,
        #         config=config["global_game_window"])
        # self.stack.add_widget(self.global_game_window)


if __name__ == '__main__':
    pass
    # app = QtWidgets.QApplication(sys.argv)
    # # app.setStyleSheet(open('./css/{0}.css'.format('base'), "r").read())
    # app.setStyleSheet(open('../css/base.css').read())
    # main = Main()
    # main.show()
    # sys.exit(app.exec_())
