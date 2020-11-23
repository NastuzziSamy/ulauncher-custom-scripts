import os

EXTENSION_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ICON_FILE = 'images/icon.png'

SCRIPT_FILE = 'scripts.json'
SCRIPT_PATH = os.path.expanduser('~/.config/ulauncher/') + SCRIPT_FILE

DEFAULT_CONFIG_PATH = EXTENSION_DIR + '/config/' + SCRIPT_FILE

MAX_SCRIPTS = 10