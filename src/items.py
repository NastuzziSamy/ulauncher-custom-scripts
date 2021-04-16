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


def generate_launcher_item(item, params):
    script = item.get('script', 'Missing script...') or 'Missing script...'

    if len(params) > 0:
        script += ' ' + ' '.join(params)
    elif len(item.get('default_arguments', [])) > 0:
        script += ' ' + ' '.join(item['default_arguments'])

    description = item['description'] + ' • ' + script if 'description' in item else script

    return ExtensionResultItem(
        icon=get_icon(item.get('icon')),
        name=item.get('name', script) or script,
        description=description,
        on_enter=RunScriptAction(script) if script else DoNothingAction()
    )


def generate_launcher_items(results, params):
    return [
        generate_launcher_item(script, params)
    for script in results]