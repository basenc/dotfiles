#!/usr/bin/env python
import json
import os
import sys
import subprocess

bt_connected = '􀑛'
#bt_idle = '􀑛'
#bt_off = '􀒝'
bt_idle = ''
bt_off = ''

rfkill_raw = os.popen('rfkill -J').read()
rfkill_json = json.loads(rfkill_raw)['']
for device in rfkill_json:
    if device['type'] == 'bluetooth' and (
            device['soft'] == 'blocked' or device['hard'] == 'blocked'):
        print(bt_off)
        sys.exit(0)
if not subprocess.call('bluetoothctl info', shell=True,
                       stdout=open(os.devnull, 'wb')):
    print(bt_connected)
else:
    print(bt_idle)
