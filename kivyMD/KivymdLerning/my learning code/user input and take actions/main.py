#https://www.youtube.com/watch?v=VqLpDaTRGLo&t=168s
#tutorial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

from kivy.lang import  Builder
from kivymd.uix.button import MDRectangleFlatButton  #kivymd button
import helpers # accessing a file in the same directory
# import gps

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette="Green" # to make green

        # username = MDTextField(text='Enter',pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                         size_hint_x=None, width=200)
        # screen.add_widget(username)
        btn=MDRectangleFlatButton(text='Sumbit',pos_hint={'center_x': 0.5, 'center_y': 0.4},

                                    on_release=self.show_data

                                  )

        #to pass the data to another function we need to add self. before variables
        self.username=Builder.load_string(helpers.username_helper) #accessing a file in the same directory
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def show_data(self, obj):
        #location =gps()

        location=[30.12,40.30]
        print(self.username.text)
        print("GPS coordinates:", location)
        screen = Screen().clear_widgets()


        return screen

DemoApp().run()
