# to add multiple item in a window , we need BoxLayout


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout # # to add multiple item in a window , we need BoxLayout


#default window color is black , but we can change it
Window.clearcolor=(1,1,1,1) #white back ground

#to resize the window, at phone size
Window.size=(360,640)


class MainApp(App):
    def build(self):
        #by default the box layout is in horijental
        #layout=BoxLayout() #making a box layout object

        #if we want to set layout in vertically
        layout = BoxLayout(orientation='vertical',spacing=10,padding=10)  # seting vertical layout
        #spacing between buttons
        btn2=Button(text="Button1", size_hint=(0.4,0.2),#button size
                  font_size='25sp',# button label text size
                  pos_hint={'center_x':0.5,'center_y':0.5}, #set the position at window
                  on_press=self.printpress,
                  on_release=self.printrelease)
        btn1=Button(text="Button2", size_hint=(0.4,0.2),#button size
                  font_size='25sp',# button label text size
                  pos_hint={'center_x':0.5,'center_y':0.5}, #set the position at window
                  on_press=self.printpress,
                  on_release=self.printrelease)
        btn3=Button(text="Button3", size_hint=(0.4,0.2),#button size
                  font_size='25sp',# button label text size
                  pos_hint={'center_x':0.5,'center_y':0.5}, #set the position at window
                  on_press=self.printpress,
                  on_release=self.printrelease)
        layout.add_widget(btn1) #adding button to layout
        layout.add_widget(btn2) #adding button to layout
        layout.add_widget(btn3)  # adding button to layout
        return layout
    def printpress(self, obj):
        print('pressed')
    def printrelease(self, obj):
        print('Button released')

MainApp().run()