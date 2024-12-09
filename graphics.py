from kivy.app import App
from kivy.lang import Builder

amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000 ]

class DealOrNoDeal(App):

    def build(self):
        return Builder.load_file('main.kv')


player_case = DealOrNoDeal()
    

DealOrNoDeal().run()

