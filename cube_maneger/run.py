#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os
import sys

import yaml
from PyQt5 import QtWidgets
import base_window


def get_config(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


config_default = "config.yaml"
config_path = os.path.join('etc', config_default)

config = get_config(config_path)

css_path = os.path.join('css', config["base"]["css_default"])


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('{}'.format(css_path), "r").read())

    m = base_window.Main(config)
    if config["base"]["fullscreen"]:
        m.showFullScreen()
    else:
        m.resize(*config["base"]["default_size"])
    m.show()
    m.add_games()

    app.exec()


if __name__ == '__main__':
    pass
    main()
