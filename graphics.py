from kivy.app import App
from kivy.lang import Builder

class DealOrNoDeal(App):

    def build(self):
        return Builder.load_file('main.kv')
    

DealOrNoDeal().run()