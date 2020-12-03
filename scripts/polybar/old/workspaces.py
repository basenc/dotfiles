#!/usr/bin/env python
import os


def split(word):
    return [char for char in word]


command = os.popen(
    "xprop -root | grep -E -e '_NET_ACTIVE_WINDOW.+:' -e '_NET_DESKTOP_NAMES.+=' -e '_NET_CURRENT_DESKTOP.+=' | sed -r 's/[^0-9x]*//g'").readlines()
command[2] = int(command[2].replace('\n', ''))
command[1] = list(map(int, split(command[1])[1:-1]))
command[0] = '0x0' in command[0]

icon = ['○', '●', '◉', '◘']
test = ['􀀸 􀀹 􀀺 􀀻 􀀼 􀀽 􀀾 􀀿 􀁀 􀁁 􀁂 􀁃 􀁄 􀁅 􀁆 􀁇 􀁈 􀁉 􀁊 􀁋 ']
desktop_match = 0

try:
    bar = [icon[0]] * 10
    for i in command[1]:
        bar[i - 1] = icon[2]
    if not command[0]:
        bar[command[1][command[2]] - 1] = icon[3]
    else:
        bar[command[1][command[2]] - 1] = icon[1]
except BaseException:
    pass

print(' '.join(bar))
