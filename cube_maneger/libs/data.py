#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

модуль предоставляет абстрактный класс Data
класс Data предоставляет "интерфейс"  load
который загружает базу из файла

в классе потомке требуется реализация метода get_data и dump

>>> data = JsonData()
>>> data.load("path")

'''

import os
import json
import shelve

class DataError(Exception): pass

_FILE_ASSERT_TEMPLATE = "файл < {} > не существует"
_METHOD_ERROR_ASSERT_TEMPLATE = "метод < {} > надо переопределить в наследнике"


class Data(dict):
    def __init__(self, path):
        """
        в классе потомке требуется реализация метода get_data
        метод должен вернуть dict
        """
        super().__init__()
        self.path = path
        assert hasattr(self, "get_data")
        assert hasattr(self, "dump")

    def load(self):
        if self:
            self.clear()
        if not os.path.isfile(self.path):
            raise FileNotFoundError(
                _FILE_ASSERT_TEMPLATE.format(self.path))

        self.update(self.get_data(self.path))

    def save(self, obj=None, path=None):
        if obj is None:
            obj = self
        elif not obj:
            raise Exception("не может быть пуст")
        if path is None:
            path = self.path
        with open(path, "w") as json_file:
            self.dump(obj, path)

class JsonData(Data):

    def get_data(self, path):
        with open(path, "r") as obj:
            return json.load(obj)

    def dump(self, obj, file):
        json.dump(obj, file, indent=2)


class ShelveData(Data):
    def get_data(self, path):
        path = os.path.splitext(path)[0]
        return shelve.open(path)


if __name__ == '__main__':
    import paths
    json_file = os.path.join(paths.get_edit_settings(),
                             "edit_settings.json")
    # shelve_file = os.path.join(paths.get_data_dir(), "dict_shl",
    #                            "secondary_geometry_shl.dat")
    #
    #
    def load(path, data_cls):
        data = data_cls(path)
        data.load()
        print(data)


    load(json_file, JsonData)
    # load(shelve_file, ShelveData)
    # import doctest
    # doctest.testmod()