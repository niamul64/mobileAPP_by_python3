# to add multiple item in a window , we need BoxLayout


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white back ground

#to resize the window, at phone size
Window.size=(360,640)

class MainApp(App):
    def build(self):
        # layout = GridLayout(cols=3)  # grid layout obj

        layout = GridLayout(cols=2,row_force_default=True, row_default_height=40)  # each of row have height of 40 px

        # size_hint is to resize the button size
        # but the button size is responsive depending on window size
        # if we want to use fixed size the we can use size_hint(None,None)
        # and we can use width=100,height=50
        btn1 = Button(text='Hello 1', size_hint=(None,None),#button size
                      width=100,height=50)
        btn2 = Button(text='Hello 2')
        btn3 = Button(text='Hello 3', size_hint=(None,None),#button size
                      width=100,height=50)
        btn4 = Button(text='Hello 4' )

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4) # adding button to layout
        return layout



    def printpress(self, obj):
        print('pressed')
    def printrelease(self, obj):
        print('Button released')

MainApp().run()