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

        params = strip_list(query.split(' '))            

        launcher = Scripts(params)

        if not launcher.has_config():
            return RenderResultListAction(no_config_items())

        if not launcher.has_query():
            return RenderResultListAction(show_used_args(launcher))

        results = launcher.execute()

        if not results:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_launcher_items(results))


if __name__ == "__main__":
    CustomSearchExtension().run()