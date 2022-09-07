import os
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, hook
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from settings.widgets import init_widgets_screen1, init_widgets_screen2
from settings.shortcuts import get_keys

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


groups = [
    Group("1", label="", layout="monadtall"),
    Group("2", label="", layout="monadtall"),
    Group("3", label="", layout="monadtall"),
    Group("4", label="", layout="monadtall"),
    Group("5", label="", layout="monadtall"),
    Group("6", label="", layout="monadtall"),
    Group("7", label="", layout="monadtall"),
    Group("8", label="", layout="monadtall"),
    Group("9", label="", layout="monadtall"),
    Group("0", label="", layout="monadtall")
]


keys = get_keys()

for i in groups:
    keys.extend([
        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin": 5,
            "border_width": 2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }


layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=5, border_width=2,
                     border_focus="#A77AC4", border_normal="#aeaeae", round=True),
    layout.MonadWide(margin=8, border_width=2,
                     border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]


def init_colors():
    from os import path
    import json
    qtile_path = path.join(path.expanduser('~'), ".config", "qtile")

    theme = "dracula"

    config = path.join(qtile_path, "config.json")
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{"theme": "{theme}"}}\n')

    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


colors = init_colors()


def init_screens():
    # w = '~/Imágenes/wallpapers/kurisu.jpg'

    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1))
    ]


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]


# Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d["1"] = ["Code", "Visual Studio Code", "VScode", "code"]
    d["2"] = ["Terminator", "terminator"]
    d["3"] = ["Firefox", "firefox", "mozilla",
              "Navigator", "Mozilla Firefox", "mozilla firefox"]
    d["4"] = ["discord", "ts3client_linux_amd64"]
    d["6"] = ["whatsapp-for-linux"]
    d["8"] = ["Nautilus", "nautilus", "Files", "files"]
    d["9"] = ["Steam"]
    d["0"] = ["TelegramDesktop", "telegram-desktop"]
    ######################################################################################

    wm_class = client.window.get_wm_class()[0]

    for key, value in d.items():
        if wm_class in value:
            group = key
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='arcolinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(title="Resize Canvas")

],  fullscreen_border_width=0, border_width=0)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
