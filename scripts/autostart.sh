#!/bin/sh

nitrogen --restore 0>/dev/null 2>&0 &
picom --config $HOME/.config/qtile/scripts/picom.conf &

python ./qtile_text.py 0>./log.txt 2>&0 & disown 
xbindkeys

