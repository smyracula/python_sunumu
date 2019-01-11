# Uygumalanın ayağa kalktığı bölüm.
from kivy.app import App
# Kivy araçları
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        return Label(text='Merhaba Millet')


# Uygulamayı başlat
TestApp().run()