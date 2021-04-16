from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.functions import strip_list
from src.items import no_config_items, no_results_item, generate_launcher_items
from src.scripts import Scripts


class CustomSearchExtension(Extension):
    def __init__(self):
        super(CustomSearchExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()
        launcher = Scripts(strip_list(query.split(' ')))

        if not launcher.has_config():
            return RenderResultListAction(no_config_items())

        if launcher.has_query():
            results, params = launcher.execute()
        else:
            results, params = launcher.get_first_scripts()

        if not results or len(results) == 0:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_launcher_items(results, params))


if __name__ == "__main__":
    CustomSearchExtension().run()