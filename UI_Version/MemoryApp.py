import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
kivy.require("1.9.1") 
Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
Window.clearcolor = (95/256, 96/256, 89/256, 1)
Window.size=(640,480)


class HomeWidget(Widget):
    pass
class MemoryApp(App): #The kv file needs to have the name as this class minus the App bit - Memory.kv
    def build(self):
        app = HomeWidget()
        return app #This pushes it to the window
if __name__ == '__main__':
    MemoryApp().run() #This must have the same name as the App
