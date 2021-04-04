
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
class DemoApp(MDApp):
    def build(self):

        i = MDLabel(text='Hello')
        return i

        # return l


DemoApp().run()