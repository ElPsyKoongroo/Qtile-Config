from libqtile import widget
from .theme import colors


def init_widgets_defaults():
    return dict(font="FontAwesome",
                fontsize=20,
                padding=2,
                background=["color4"][0])


widget_defaults = init_widgets_defaults()

# Return my standar separator
def sep():
    return widget.Sep(
        linewidth = 3,
        padding = 15,
        foreground = colors["grey"][0],
        background = colors["dark"][1]
    )

def arrow_sep(bcolor, fcolor):
    return widget.TextBox(
        font="JetBrains Mono NL",
        text='◀',
        background=bcolor, #colors["color4"][0],
        foreground=fcolor,
        padding=0,
        fontsize=39
    )

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font="Font Awesome 6 Free",
            fontsize=14,
            margin_y=1,
            margin_x=0,
            padding_y=6,
            padding_x=5,
            borderwidth=0,
            disable_drag=True,
            active=colors["active"][0],
            inactive=colors["blue"][0],
            rounded=False,
            highlight_method="text",
            this_current_screen_border=colors["focus"][0],
            foreground=colors["dark"],
            background=colors["dark"]
        ),

        sep(),
        widget.CurrentLayout(
            font="Noto Sans Bold",
            foreground=colors["grey"][0],
            background=colors["dark"]
        ),
        sep(),

        widget.WindowName(
            font="FontAwesome",
            fontsize=12,
            foreground=colors["green"][0],
            background=colors["dark"],
            padding=0
        ),

        widget.Systray(
            background=colors["dark"],
            icon_size=20,
            padding=4
        ),

        arrow_sep(colors["dark"], colors["orange"]),
        widget.TextBox(
            font="FontAwesome",
            name="hack",
            text="sergious234 ",
            background=colors["orange"],
            foreground=colors["dark"],
            padding=0,
            fontsize=13
        ),

        arrow_sep(colors["orange"], colors["red"]),
        widget.TextBox(
            font="FontAwesome",
            name="cpu",
            text=" Intel Core i7-4771",
            foreground=colors["dark"][0],
            background=colors["red"],
            padding=0,
            fontsize=13
        ),

        arrow_sep(colors["red"], colors["color3"]),
        widget.TextBox(
            font="FontAwesome",
            name="Volume_icon",
            text=" ",
            fontsize=19,
            background=colors["color3"],
            foreground=colors["dark"],
            padding=0,
        ),
        widget.Volume(
            device="default",
            channel="Master",
            update_interval=0.2,
            background=colors["color3"],
            foreground=colors["dark"],
        ),

        arrow_sep(colors["color3"], colors["purple"]),
        widget.Net(
            font="JetBrains Mono NL",
            fontsize=12,
            prefix="k",
            format="Telekeibol {up}↑ {down}↓ ",
            interface="enp3s0",
            foreground="#000000", #colors["color2"][0],
            #background=colors["dark"],
            background=colors["purple"][0],
            padding=0,
        ),

        arrow_sep(colors["purple"], colors["green"]),
        widget.Clock(
            foreground=colors["dark"][0],
            background=colors["green"],
            fontsize=12,
            format="%Y-%m-%d %H:%M"
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2: list = init_widgets_list()
    del widgets_screen2[5]
    return widgets_screen2

widgets_screen2 = init_widgets_screen2()
widgets_screen1 = init_widgets_screen1()
