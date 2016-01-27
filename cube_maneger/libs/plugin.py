#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import sys
from importlib import import_module

from PyQt4 import QtGui

_plugin_dir = "game_plugin"
_mod_name = "game"
_class_name = "GamePlugin"


class ErrorIndex(Exception): pass


class ErrorChange(Exception): pass


class ErrorType(Exception): pass


class ErrorAbstract(Exception): pass


_ERROR_CHANGE_MESSAGE = "нельзя изменить атрибут"


class WidgetPlugin(QtGui.QFrame):
    def __init__(self, name, root_path, index, tool_btn_name, style_file):
        super().__init__()
        self.name = name
        self.root_path = root_path
        self.index = index
        self.tool_btn_name = tool_btn_name
        self.style_file = style_file

    def css_file(self, root, dir, file):
        return os.path.join(root, dir, file)

    @property
    def home_btn(self):
        raise ErrorAbstract(
            "должно вернуть ссылку на кнопку отвечающую за возврат в меню")

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        if i != 0:
            self._index = i
        else:
            raise ErrorIndex("индекс не может быть 0")

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, path):
        self._root_path = path

    def __repr__(self):
        return '''
        object - {}
        index - {}
        tool_icon - {}'''.format(
            self.__class__.__name__,
            self.index, self.tool_icon)


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
            if not isinstance(obj, WidgetPlugin):
                raise ErrorType(
                    "плагин должен быть унаследован от WidgetPlugin")
            objects.append(obj)
        return tuple(objects)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = WidgetPlugin()
    main.show()
    sys.exit(app.exec_())
