import os

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction

from src.consts import ICON_FILE, SCRIPT_PATH

def no_config_items():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No scripts',
            description='Add scripts in ' + SCRIPT_PATH,
            on_enter=RunScriptAction('xdg-open ' + SCRIPT_PATH)
        )
    ]


def no_results_item():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No results',
            on_enter=DoNothingAction()
        )
    ]


def get_icon(icon):
    icon = icon or ICON_FILE

    if icon.startswith('~'):
        icon = os.path.expanduser(icon)
    
    if not icon.startswith('/') or not os.path.exists(icon):
        return ICON_FILE

    return icon 


def generate_launcher_item(script):
    path = script.get('path', 'Missing path...') or 'Missing path...'

    return ExtensionResultItem(
        icon=get_icon(script.get('icon')),
        name=script.get('name', path) or path,
        description=script.get('description', path) or path,
        on_enter=RunScriptAction(path) if path else DoNothingAction()
    )


def generate_launcher_items(results):
    return [
        generate_launcher_item(script)
    for script in results]