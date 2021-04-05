#https://www.youtube.com/watch?v=VqLpDaTRGLo&t=168s
#tutorial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.lang import  Builder
from kivymd.uix.button import MDRectangleFlatButton  #kivymd button
import helpers # accessing a file in the same directory
from kivymd.uix.label import MDLabel, MDIcon
# import gps
Window.clearcolor=(1,1,1,1) #white back ground

#to resize the window, at phone size
Window.size=(360,640)
class DemoApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette="Green" # to make green

        # username = MDTextField(text='Enter',pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                         size_hint_x=None, width=200)
        # screen.add_widget(username)
        btn=MDRectangleFlatButton(text='Sumbit',pos_hint={'center_x': 0.5, 'center_y': 0.4},

                                    on_release=self.show_data

                                  )

        #to pass the data to another function we need to add self. before variables
        self.username=Builder.load_string(helpers.username_helper) #accessing a file in the same directory
        self.screen.add_widget(self.username)
        self.screen.add_widget(btn)
        return self.screen

    def show_data(self, obj):
        #location =gps()
        #analysis
        location=[30.12,40.30]
        print(self.username.text)
        print("GPS coordinates:", location)
        self.screen.clear_widgets()
        label1 = MDLabel(text="You mobile number: " + str(self.username.text),
                        halign="center", pos_hint={'center_x': 0.5, 'center_y': 0.9}, theme_text_color="Error",
                        font_style="Subtitle2")
        I = Image(source='Capture.png', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        label = MDLabel(text="Your GPS coordinates: ("+ str(location[0])+"," + str(location[1])+")", halign="center", pos_hint={'center_x': 0.5, 'center_y': .82}, theme_text_color="Error",
                        font_style="Subtitle2")
        I=Image(source='Capture.png')
        label2 = MDLabel(text="Danger level: 90%",
                        halign="center", pos_hint={'center_x': 0.5, 'center_y': 0.86}, theme_text_color="Error",
                        font_style="Subtitle2")
        label3 = MDLabel(text="location status: You are in red zone",
                         halign="center", pos_hint={'center_x': 0.5, 'center_y': 0.79}, theme_text_color="Error",
                         font_style="Subtitle2")
        I = Image(source='Capture.png')

        self.screen.add_widget(label1)
        self.screen.add_widget(label)
        self.screen.add_widget(label2)
        self.screen.add_widget(label3)

        self.screen.add_widget(I)



DemoApp().run()
