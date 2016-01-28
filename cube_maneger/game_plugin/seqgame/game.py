#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtWidgets

from cube_maneger.game_plugin.seqgame import conf as cfg
from cube_maneger.libs import plugin

root_path = os.path.dirname(__file__)


class GamePlugin(plugin.WidgetPlugin):
    def __init__(self):
        super().__init__(cfg.object_name, root_path, cfg.index,
                         cfg.tool_object_name, cfg.style_name)
        self.name = cfg.object_name
        self.root_path = root_path
        self.index = cfg.index
        self.tool_btn_name = cfg.tool_object_name
        self.setObjectName(self.name)
        self.style_file = cfg.style_name

        self.exit_btn = QtWidgets.QPushButton("EXIT", self)

        self.css_path = os.path.join(self.root_path, cfg.style_dir,
                                 self.style_file)
        self.setStyleSheet(open('{}'.format(self.css_path), "r").read())

    @property
    def home_btn(self):
        return self.exit_btn

    def __doc__(self):
        return "{}".format(plugin.WidgetPlugin)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())
