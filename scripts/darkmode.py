#!/usr/bin/env python

from os import environ
from sys import exit
from pathlib import Path
from yaml import safe_load as yaml_load
from yaml import dump as yaml_dump
from argparse import ArgumentParser
from plumbum import FG, colors
from plumbum.cmd import echo

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


def set_alacritty(colorscheme):
    print('Setting alacritty...', end='')
    print(colors.green | 'Done!')
    pass

def set_polybar(colorscheme):
    print('Setting polybar...', end='')
    print(colors.green | 'Done!')
    pass

def set_dunst(colorscheme):
    print('Setting dunst...', end='')
    print(colors.green | 'Done!')
    pass

def set_i3(colorscheme):
    print('Setting i3...', end='')
    print(colors.green | 'Done!')
    pass

def set_rofi(colorscheme):
    print('Setting rofi...', end='')
    print(colors.green | 'Done!')
    pass

colorschemes_functions = [set_alacritty, set_polybar, set_dunst, set_i3, set_rofi]


def apply_theme(themes):
    pass

def apply_icons(icons):
    pass

def reload_configs():
    pass


parser = ArgumentParser(description='Change system colors and theme.')
parser.add_argument('profile', metavar='PROFILE', type=str,
                    help='Which profile to apply')
parser.add_argument('-f', '--force', action='store_true',
                    help='Force apply profile')
args = parser.parse_args()

config_path = Path(environ['DOTFILES']) / 'config.yaml'
settings = yaml_load(read_file(config_path))

if settings["profiles"]["current"] == args.profile and not args.force:
    print(colors.green | "Profile is already set.")
elif args.profile in settings["profiles"]:
    settings["profiles"]["current"] = args.profile

    print(colors.blue | 'Applying coloschemes...')
    for function in colorschemes_functions:
        function(settings["profiles"][args.profile]["colors"])

    print(colors.blue | 'Applying themes...')
    apply_theme(settings["profiles"][args.profile]["themes"])

    print(colors.blue | 'Applying icons...')
    apply_icons(settings['profiles'][args.profile]['icons'])

    print(colors.blue | 'Reloading...')
    reload_configs()

    write_file(config_path, yaml_dump(settings))
else:
    print(colors.red | "This profile does not exist!")
    exit(1)
