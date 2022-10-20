import math
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.config import Config

Config.set('graphics', 'width', '920')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)

def half_interval(a, b):
    """Метод ділить інтервал навпіл"""
    return (a + b) / 2

def func(x):
    """
    Обчислимо значення функції
    3x - cosX - 1 = 0
    """
    return 3 * x - math.cos(x) - 1

def core(a,b,E):
        #Ядро программи
        #a,b,E will be changed from MainWindow(scene) class
        counter = 0
        output = ""
        max_counter = 200
        while abs(b - a) > E:
            counter += 1
            if counter >= max_counter:
                print('Забагато кроків')
                break
            if abs(b - a) <= E:
                print('Значення math.abs(b-a) стало меньше ніж E')
                break

            print('\n\n Step №{counter}'.format(counter=counter))
            output += '\n\n Step №{counter}'.format(counter=counter)
            
            fa = func(a)
            c = half_interval(a, b)
            fc = func(c)
            if fa * fc >= 0:
                a = c
            else:
                b = c
            print('fa = {f_a} fc = {f_c} fa * fc = {res}'.format(f_a=fa, f_c=fc, res=fa * fc))
            output += 'fa = {f_a} fc = {f_c} fa * fc = {res}'.format(f_a=fa, f_c=fc, res=fa * fc)
            print('a = {a} b = {b}'.format(a=a, b=b))
            output += 'a = {a} b = {b}'.format(a=a, b=b)

        #Output popup
        box = BoxLayout(orientation = "vertical")
        box.add_widget(Label(text="Answer: "+output,font_size=15, size_hint=(1,0.4)))

        close_button = Button(text='Close',font_size=20, size_hint=(1,0.1), size_hint_y=None)
        box.add_widget(close_button)
        out_popup = Popup(content=box,title="Answer", auto_dismiss=False,size_hint=(0.9, 0.9), size=(400, 200))
        close_button.bind(on_press=out_popup.dismiss)
        out_popup.open()
    

#Define screens
class MainWindow(Screen):
    #Def who return action when ConfirmButton is being pressed
    def on_confirm(self):
        if(self.ids.input_id1.text or self.ids.input_id2.text or self.ids.input_id3.text != "" and self.ids.input_id3.text != int):
            #Creating input
            #Обчислення після отриманих змінних відбуваются в "core" функції, змінні передаються туди ж
            core(a=int(self.ids.input_id1.text), b=int(self.ids.input_id2.text), E=float(self.ids.input_id3.text))
        else:
            print("Error")
            Newton.stop()
        

#Required initiation of screens
class WindowManager(ScreenManager):
    pass

#Loading kivy gesign file
kv = Builder.load_file("UI.kv")            

#Core of application
class Newton(App):
    def build(self):
        return kv

#Run App Class
if __name__ == "__main__":
    Newton().run()
