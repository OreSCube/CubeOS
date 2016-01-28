#!/usr/bin/env python
# -*- coding: utf-8 -*-



from os.path import dirname, join

root_path = dirname(__file__)

resource = "resource"
icons = "icons"
tool_name_icon = "tool.png"
tool_name_icon_hover = "tool_hover.png"
tool_name_icon_pressed = "tool_pressed.png"
style_name = "base.css"
style_dir = "css"


icons_path = join(root_path, resource, icons)

object_name = "seqgame"
tool_object_name = "seqgametool"
style_path = join(root_path, style_name)
tool_icon = join(icons_path, tool_name_icon)
tool_icon_hover = join(icons_path, tool_name_icon_hover)
tool_icon_pressed = join(icons_path, tool_name_icon_pressed)
index = 1
