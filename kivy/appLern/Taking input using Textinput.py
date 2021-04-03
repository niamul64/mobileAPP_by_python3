# to add multiple item in a window , we need BoxLayout


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white back ground

#to resize the window, at phone size
Window.size=(360,640)

class MainApp(App):
    def build(self):

        layout=GridLayout(cols=2,row_force_default=True, row_default_height=40, spacing=20,padding=20)

        # when ever we passing values to other method we have to add 'self.'
        self.weight =TextInput(text='Enter Value here')
        self.height =TextInput(text='Enter Value here')
        submit= Button(text='Submit', on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout


    def submit(self, obj):
        print("weight:"+self.weight.text)
        print("height:" + self.height.text)
    def printpress(self, obj):
        print('pressed')
    def printrelease(self, obj):
        print('Button released')

MainApp().run()