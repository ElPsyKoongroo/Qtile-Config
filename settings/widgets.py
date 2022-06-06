from libqtile import widget
from .theme import colors
import os

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=["color4"][0])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
                widget.GroupBox(
                        font="FontAwesome",
                        fontsize = 16,
                        margin_y = -1,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors["active"][0], 
                        inactive = colors["inactive"][0],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors["focus"][0],
                        foreground = colors["dark"],
                        background = colors["dark"]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors["grey"][0],
                        background = colors["dark"]
                        ),
                widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors["grey"][0],
                        background = colors["dark"]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors["grey"][0],
                        background = colors["dark"]
                        ),
                widget.WindowName(
                        font="FontAwesome",
                        fontsize = 12,
                        foreground = colors["color5"][0],
                        background = colors["dark"],
                        padding=0
                        ),
                widget.TextBox(
                        font="FontAwesome",
                        text="sergious234 ",
                        foreground=colors["light"][0],
                        background=colors["dark"],
                        padding = 0,
                        fontsize=13
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 20,
                        foreground = colors["grey"][0],
                        background = colors["dark"]
                        ),
                widget.TextBox(
                        font="FontAwesome",
                        name="cpu",
                        text="i7 4771 ",
                        foreground=colors["light"][0],
                        background=colors["dark"],
                        padding = 0,
                        fontsize=13
                    ),
                widget.Sep(
                        linewidth = 2,
                        padding = 20,
                        foreground = colors["grey"][0],
                        background = colors["dark"]
                        ),
                widget.Net(
                        font="Noto Sans",
                        fontsize=12,
                        prefix="k",
                        format="Telekeibol {up}↑ {down}↓",
                        interface="enp3s0",
                        foreground=colors["light"][0],
                        background=colors["dark"],
                        padding = 0,
                        ),
                widget.Clock(
                            foreground = colors["light"][0],
                            background = colors["dark"],
                            fontsize = 12,
                            format="%Y-%m-%d %H:%M"
                            ),
                widget.Systray(
                            background=colors["dark"],
                            icon_size=20,
                            padding = 4
                            ),
            ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

widgets_screen1 = init_widgets_screen1()