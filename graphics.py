from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
import random


class DealOrNoDeal(App):

    def build(self):
        
        Builder.load_file('main.kv')

        self.layout = BoxLayout(orientation = "vertical")

        self.buttons_list = []
    
        self.amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000 ]

        for button in self.layout.children:
            if isinstance(button, Button):
                button_value = self.amounts[random.randint(0,len(self.amounts) + 1)]
                self.buttons_list.append((button, button_value))
                self.amounts.remove(button_value)

        for button in self.buttons_list:

    



class Screen2(Screen):

    def build(self):
        
        

        for value in self.amounts:
            self.amounts.remove(value)

        return BoxLayout()
    

    
if __name__ == "__main__":
    DealOrNoDeal().run()

