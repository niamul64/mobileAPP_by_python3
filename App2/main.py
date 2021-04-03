from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        #l=MDLabel(text="hello", halign='center', theme_text_color='Error')
        #l = MDLabel(text="hello", halign='center', theme_text_color='Custom',text_color=(0,1,0,1))
        #l = MDLabel(text="hello", halign='center',theme_text_color='Custom',text_color=(0,0,1,1))
        #https://github.com/attreyabhatt/KivyMD-Basics/blob/master/2%20-%20Labels/notes.txt   color and text styles
        l = MDLabel(text="hello", halign='center', theme_text_color='Custom', text_color=(0, 0, 1, 1))
        return l


DemoApp().run()