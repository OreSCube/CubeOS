#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtWidgets


from cube_maneger.libs import plugin

root_path = os.path.dirname(__file__)

config = plugin.get_config(root_path)


class GamePlugin(plugin.GamePlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        # self.style_file = cfg.style_name
        #
        # self.exit_btn = QtWidgets.QPushButton("EXIT", self)
        #
        # self.css_path = os.path.join(self.root_path, cfg.style_dir,
        #                          self.style_file)
        # self.setStyleSheet(open('{}'.format(self.css_path), "r").read())

    # @property
    # def home_btn(self):
    #     return self.exit_btn
    #
    # def __doc__(self):
    #     return "{}".format(plugin.GamePlugin)
    #
    # def __call__(self, *args, **kwargs):
    #     return self

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())
