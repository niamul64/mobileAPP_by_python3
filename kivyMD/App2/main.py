from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class DemoApp(MDApp):
    def build(self):
        #l=MDLabel(text="hello", halign='center', theme_text_color='Error')
        #l = MDLabel(text="hello", halign='center', theme_text_color='Custom',text_color=(0,1,0,1))
        #l = MDLabel(text="hello", halign='center',theme_text_color='Custom',text_color=(0,0,1,1))
        #https://github.com/attreyabhatt/KivyMD-Basics/blob/master/2%20-%20Labels/notes.txt   color and text styles
        # l = MDLabel(text="Hello", halign='center', theme_text_color='Custom', text_color=(0, 0, 1, 1),
        #             font_style='H1')
        # l = MDLabel(text="Hello", halign='center', theme_text_color='Custom', text_color=(0, 0, 1, 1),
        #              font_style='Caption')
        # i = MDIcon(icon='language-python', halign='center')
        i = MDIcon(icon='laptop-off', halign='center')
        return i

        # return l


DemoApp().run()