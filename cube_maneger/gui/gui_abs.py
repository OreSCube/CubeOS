#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
модуль предаставляет классы наслдеованые от qt классов для использования в основной программе
"""


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QObject

_box_margin = (1, 10, 21, 1)
_box_spacing = 10

class AbsGui(QObject):
    def __init__(self, name, parent):
        super().__init__()
        self.setObjectName(name)
        self.setParent(parent)





class Box(QtWidgets.QBoxLayout):
    _horizontal = QtWidgets.QBoxLayout.LeftToRight
    _vertical = QtWidgets.QBoxLayout.TopToBottom

    def __init__(self, direction, QWidget_parent=None,
                 margin=_box_margin, spacing=_box_spacing):
        """

        :param direction: Box._horizontal \ Box._vertical
        :param QWidget_parent: QWidget
        :param margin: поле вокруг
        :param spacing: интервал (шаг) между виджетами
        """
        super().__init__(direction, QWidget_parent)
        self.setDirection(direction)
        self.setContentsMargins(*margin)
        self.setSpacing(spacing)


class Frame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)


class StackedLayout(QtWidgets.QStackedLayout):
    def __init__(self, parent=None, *__args):
        super().__init__(*__args)


    def add_widget(self, QWidget):
        self.addWidget(QWidget)

class MenegerFrame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)

class ToolGame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)

class SettingButton(QtWidgets.QPushButton, AbsGui):
    def __init__(self, name, parent, size):
        """

        :type size_button: int
        :type size_icon: int
        :type name: str
        """
        super().__init__(name, parent)
        self.setIconSize(QtCore.QSize(size, size))
        self.setFixedSize(size + 2, size + 2)

class GameButton(QtWidgets.QToolButton, AbsGui):
    def __init__(self, name, parent, index):
        super().__init__(name, parent,)
        self.index = index

    def __repr__(self):
        return """
        object - {};
        object_name - {};
        index - {}
        """.format(self.__class__.__name__, self._name, self.index)