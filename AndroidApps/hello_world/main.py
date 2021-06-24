
"""
    to install kivy

    python3 -m pip install --pre kivy[base] kivy_examples
"""

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello world!")

if __name__ == '__main__':
    MyApp().run()