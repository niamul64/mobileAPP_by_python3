
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white


class MainApp(App):
    def build(self):

        b=Button(text="Button", size_hint=(0.15,0.1),#button size
                  font_size='25sp',# button label text size
                  pos_hint={'center_x':0.5,'center_y':0.5}, #set the position at window
                  on_press=self.printpress,
                  on_release=self.printrelease)
        return b
    def printpress(self, obj):
        print('pressed')
    def printrelease(self, obj):
        print('Button released')

MainApp().run()