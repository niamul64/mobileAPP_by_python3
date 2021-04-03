
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white


class MainApp(App):
    def build(self):
        # return Label(text="Hello World",font_size='20sp',bold=True,italic=True)
        # return Label(text="Hello World", font_size='20sp', bold=True,
        #              color=(0,0,0,1),italic=True)
        l=Label(text="Hello World", font_size='20sp', bold=True,
                color=(0,0,0,1),italic=True)
        return l
MainApp().run()