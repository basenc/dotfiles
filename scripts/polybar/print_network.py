#!/usr/bin/env python
import os
import re

icons = {
    'wifi': '􀙇',
    'eth': '􀜡',
    'p2p': '􀙧',
    'bridge': '􀢹',
    'tun': '􀙧'
}

fields = [
    "GENERAL.DEVICE",
    "GENERAL.STATE",
    "GENERAL.TYPE",
    "GENERAL.CONNECTION",
    "IP4.ADDRESS",
    "IP4.GATEWAY",
    "IP4.DNS",
    "IP6.ADDRESS"]
devices = os.popen(
    "nmcli --get-values GENERAL.DEVICE d show").read().split('\n\n')

span_grayed_prefix = '<span foreground="gray">'
span_grayed_suffix = '</span>'

properties = []
entries = [[]]

for device in devices:
    properties = os.popen(
        "nmcli --escape no --get-values " +
        ','.join(fields) +
        ' d show ' +
        device).read().split('\n')[
        :-
        1]
    properties += [''] * (len(fields) - len(properties))

    if '100' in properties[1]:
        entry = []
        if properties[2] == 'wifi':
            entry.append(
                'Type\t\t\tWireless %s (%s)' %
                (icons['wifi'], properties[0]))
        elif properties[2] == 'ethernet':
            entry.append(
                'Type\t\t\tEthernet %s (%s)' %
                (icons['eth'], properties[0]))
        elif properties[2] == 'p2p':
            entry.append(
                'Type\t\t\tPoint to point %s (%s)' %
                (icons['p2p'], properties[0]))
        elif properties[2] == 'bridge':
            entry.append(
                'Type\t\t\tBridge %s (%s)' %
                (icons['bridge'], properties[0]))
        elif properties[2] == 'tun':
            entry.append(
                'Type\t\t\tTunnel %s (%s)' %
                (icons['tun'], properties[0]))

        if properties[3]:
            entry.append('Connected to\t%s' % properties[3])
        if properties[4]:
            entry.append('IPv4 Address\t%s' % properties[4])
        if properties[5]:
            entry.append('IPv4 Gateway\t%s' % properties[5])
        if properties[6]:
            entry.append(
                'DNS Servers\t%s' %
                properties[6].replace(
                    ' | ',
                    '\n\t\t\t\t'))
        if properties[7]:
            entry.append('IPv6 Address\t%s' % properties[7])
        entries.append('\n'.join(entry))

if len(entries) >= 2:
    print('\n\n'.join(entries[1:]))
else:
    print('<span foreground="gray">Network unaviable</span>')
