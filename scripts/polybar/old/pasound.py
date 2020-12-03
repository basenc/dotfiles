#!/usr/bin/env python
import os

command = os.popen(
    "pacmd list-sinks | sed -e 's/[[:blank:]]//g' -n -e '/*index:/,/activeport:/p' | grep -e 'index:' -e 'muted:' -e 'volume:' -e 'activeport:'").read()
sink_list = command.replace('\n', ':').replace('/', ':').split(':')
sink_index = sink_list[1]
sink_muted = sink_list[15]
sink_volume = int(sink_list[4])
sink_device = sink_list[17]

circles = ["○\u200A", "◔\u200A", "◐\u200A", "◕\u200A", "●\u200A"]
icon_mute = ""
icon_default = ""
icon_headphones = ""
icon_headset = ""
dots = 5


def progressBar(progress, maximum, divs, icons):
    bar = ""
    num_of_filled = (progress / maximum) * divs
    if progress == maximum:
        bar += icons[-1] * divs
    else:
        bar += icons[-1] * int(num_of_filled)
        bar += icons[int((num_of_filled % 1) * len(icons))]
        bar += icons[0] * (divs - int(num_of_filled) - 1)
    return bar


if sink_muted == 'yes':
    print(icon_mute)
else:
    print(icon_default, progressBar(sink_volume, 65536, dots, circles), end='')
    if sink_device == '<analog-output-headphones>':
        print('\u200A' + icon_headphones, end='')
    elif sink_device == '<headset-output>':
        print('\u200A' + icon_headset, end='')
    elif sink_device == '<analog-output-speaker>':
        pass
    else:
        pass
