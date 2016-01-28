#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore

import gui_abs as gui


class GameBox(gui.Frame):
    def __init__(self, name, parent, spacing=0, margin=(0, 0, 0, 0)):
        super().__init__(name, parent)
        self.box = gui.Box(gui.Box._vertical, self, margin=margin,
                           spacing=spacing)
        self.box.setAlignment(
                QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

    def create_button(self, name, index, icon_size):
        button = gui.GameButton(name, self, index)
        button.setIconSize(
                QtCore.QSize(icon_size, icon_size))
        self.box.insertWidget(index, button)
        return button

class Display(gui.ToolGame):
    def __init__(self, name, parent):
        super().__init__(name, parent)

class MangerWindow(gui.MenegerFrame):
    def __init__(self, name, parent, config, visual_parent):
        super().__init__(name, parent)
        self.cfg = config
        self.parent = parent
        self.setParent(visual_parent)

        self.tool_game_box = GameBox("tool_game", self,
                                     spacing=self.cfg[
                                         "game_tool_spacing"],
                                     )

        self.setting_widget = Display("setting_box", None)

        self.display_widget = gui.ToolGame("display", None)

        self.exit = gui.SettingButton("exit_button", None,
                                      self.cfg["icon_setting_size"])
        self.volume = gui.SettingButton("volume_button", None,
                                        self.cfg["icon_setting_size"])
        self.config = gui.SettingButton("config_button", None,
                                        self.cfg["icon_setting_size"])

        display_layout = gui.Box(gui.Box._vertical, None,
                                 self.cfg["display_layout_margin"], 0)
        box_base = gui.Box(gui.Box._horizontal, self,
                           self.cfg["base_layout_margin"], 0)
        self.setting_layout = gui.Box(gui.Box._horizontal,
                                      QWidget_parent=self.setting_widget,
                                      spacing=self.cfg[
                                          "spacing_setting"],
                                      margin=self.cfg[
                                          "setting_layout_margin"])

        box_base.addWidget(self.tool_game_box,
                           self.cfg["stretch_game_tool"])
        box_base.addLayout(display_layout,
                           self.cfg["stretch_display_layout"])
        display_layout.addWidget(self.display_widget,
                                 self.cfg["stretch_display_widget"])
        display_layout.addWidget(self.setting_widget,
                                 self.cfg["stretch_setting_widget"])

        self.add_setting_buttons()
        self.set_actions_setting_buttons()

    def add_setting_buttons(self):
        self.setting_layout.addStretch(0)
        self.setting_layout.insertWidget(-1, self.config)
        self.setting_layout.insertWidget(-1, self.volume)
        self.setting_layout.insertWidget(-1, self.exit)
        self.setting_layout.addStretch(0)


    def set_actions_setting_buttons(self):
        self.parent.register_control(self.exit, "exit")

    def create_game_button(self, name, index):
        return self.tool_game_box.create_button(name, index, self.cfg[
            "icon_game_size"])
