#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import yaml
from importlib import import_module

from PyQt5 import QtWidgets

_PLUGIN_DIR = "game_plugin"
_MOD_NAME = "game"
_CLASS_NAME = "GamePlugin"
_ETC_DIR = "etc"
_CSS_DIR = "css"
_RESOURCE_DIR = "resource"
_ICONS_DIR = "icons"
_CONFIG_FILE = "config.yaml"


class ErrorIndex(Exception): pass


class ErrorChange(Exception): pass


class ErrorType(Exception): pass


class ErrorAbstract(Exception): pass


_ERROR_CHANGE_MESSAGE = "нельзя изменить атрибут"

def get_config(root):
    path = os.path.join(root, _ETC_DIR, _CONFIG_FILE)
    with open(path, "r") as obj:
        return yaml.load(obj)

class GamePlugin(QtWidgets.QFrame):
    def __init__(self, **kwargs):
        super().__init__()
        self.config = dict()
        self.config_lst = (
        'name', 'index', 'tool_btn_name', 'style_name')
        for opt in self.config_lst:
            self.config[opt] = kwargs[opt]

        self.setObjectName(self.config['name'])


    def __repr__(self):
        return '''
        object - {}
        options - {}
        '''.format(
                self.__class__.__name__, self.config)


class AdapterPluginsGame:
    mod_ext = ".py"

    def __init__(self, plugin_dir, mod_name, class_name):
        """
        :param plugin_dir: относительный путь к пакету с плагинами
        :param mod_name: имя подключаемого модуля без расширения
        :param class_name: имя подключаемого класса
        """
        self.class_name = class_name
        self.mod_name = mod_name
        self.plugin_dir = plugin_dir

    @property
    def paths(self):
        mod_list = []
        pkg_list = [p for p in glob.glob(self.plugin_dir + "/*")]
        for p in pkg_list:
            mod_list.extend(glob.glob("".join(
                    [p, os.sep, "*", self.mod_name + self.mod_ext])))
        return mod_list

    def plugin_objects(self, path_list_plug):

        """
        относительные пути к плагинам
        @:param path_list_plug: list -> str
        @:rtype: tuple -> PyQt4.QtCore.pyqtWrapperType
        """

        objects = []
        for p in path_list_plug:
            m = p[:-3].replace(os.sep, ".")
            mod = import_module(m)
            obj = getattr(mod, self.class_name)()
            if not isinstance(obj, GamePlugin):
                raise ErrorType(
                        "плагин должен быть унаследован от WidgetPlugin")
            objects.append(obj)
        return tuple(objects)
