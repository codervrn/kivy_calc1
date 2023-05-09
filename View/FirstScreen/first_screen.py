from View.base_screen import BaseScreenView
from kivymd.uix.textfield import MDTextField

from kivy.properties import StringProperty

from kivymd.icon_definitions import md_icons
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox


class MDCapitalInput(MDTextField):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.xchars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '.']

    def on_text(self, instance, value):

        print('The widget', instance.text, 'have:', value)
        #if (self.text != 'asdf'):
        #    self.text ='asdf'


    #def insert_text(self, substring, from_undo=True):
        #if (substring in self.xchars):
        #    super().insert_text(substring, from_undo=from_undo)
        #else:
        #    super().insert_text('', from_undo=from_undo)
        #print(self.text)
        #self.text='(+7)-961-613-83-10'
        #return super().insert_text('', from_undo=from_undo)


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''



class FirstScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def calculation(self, *args):
        #print(self.ids.slg1.text)
        try:
            self.ids.slg3.text=str(float(self.ids.slg1.text)+float(self.ids.slg2.text))
        except:
            pass

    def onTouch(self):
        #print(dir(self.ids.scroll.on_children))
        #print(dir(self.ids.scroll))
        pass

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
            )
        #self.manager_screens.current = 'second screen'

