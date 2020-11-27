import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

import os
os.environ["KIVY_AUDIO"] = "sdl2"

# Requiere python -m pip install ffpyplayer en linux


kv = Builder.load_file("kv.kv")

class MainWid(ScreenManager):

    def Bievenidos(self):
        sound = SoundLoader.load('notas/Bievenidos.wav')
        if sound:
            sound.play()

    def Mi(self):
        sound = SoundLoader.load('notas/Mi.wav')
        if sound:
            sound.play()

    def La(self):
        sound = SoundLoader.load('notas/La.wav')
        if sound:
            sound.play()

    def Re(self):
        sound = SoundLoader.load('notas/Re.wav')
        if sound:
            sound.play()

    def Sol(self):
        sound = SoundLoader.load('notas/Sol.wav')
        if sound:
            sound.play()

    def Si(self):
        sound = SoundLoader.load('notas/Si.wav')
        if sound:
            sound.play()

    def Mip(self):
        sound = SoundLoader.load('notas/Mip.wav')
        if sound:
            sound.play()


class UnaScreen(Screen):
    pass

class MainApp(App):

    title = "Screen Manager"

    def build(self):
        return MainWid()

if __name__ == "__main__":
    MainApp().run()