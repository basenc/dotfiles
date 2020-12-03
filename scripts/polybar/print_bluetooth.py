#!/usr/bin/env python
import os
import re

icons = {
    'audio-card': '􀑈  Headset',
    'input-gaming': '􀛹  Gamepad'
}

output = []

if devices := os.popen(
        "bluetoothctl paired-devices | awk '{print $2}'").read().rsplit('\n')[:-1]:
    for device in devices:
        info = os.popen("bluetoothctl info " + device).read()
        if re.search(r'\sConnected: yes', info):
            name = re.search(r'\sName: (.+)', info).group(1)
            _type = re.search(r'\sIcon: (.+)', info).group(1)
            output.append(
                'Name\t%s\nType\t%s\nMAC\t%s' %
                (name, icons[_type], device))
else:
    print("<span foreground='gray'>No paired devices</span>")
    exit(0)

if output:
    print('\n\n'.join(output))
else:
    print("<span foreground='gray'>No connected devices</span>")
