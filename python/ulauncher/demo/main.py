from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        for i in range(5):
            # items.append(ExtensionResultItem(icon='images/icon.png',
            #                                  name='Item %s' % i,
            #                                  description='Item description %s' % i,
            #                                  on_enter=HideWindowAction()))
            on_enter_data = {'new_name': 'Item %s was clicked' % i}
            on_alt_enter_data = {'new_name': 'Item %s was alt-entered' % i}
            items.append(ExtensionSmallResultItem(
                icon='images/icon.png',
                name='Item %s' % i,
                description='Item description %s' % i,
                on_enter=ExtensionCustomAction(on_enter_data, keep_app_open=True),
                on_alt_enter=ExtensionCustomAction(on_alt_enter_data, keep_app_open=True)
            ))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        # event is instance of ItemEnterEvent

        data = event.get_data()
        # do additional actions here...

        # you may want to return another list of results
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=data['new_name'],
                                                           on_enter=HideWindowAction())])


if __name__ == '__main__':
    DemoExtension().run()
