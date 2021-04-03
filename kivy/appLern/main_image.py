
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image,AsyncImage
from kivy.core.window import Window
#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white


class MainApp(App):
    def build(self):

        # Ima=Image(source='Capture.png')
        Ima = AsyncImage(source='https://img.lovepik.com/original_origin_pic/18/06/18/ced3ec343bf186335c5b268535a3a797.png_wh300.png')
#tutorial: https://www.youtube.com/watch?v=ocGVGZ8pmls
        return Ima
MainApp().run()