from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

from random import randint


class iu(BoxLayout):
    def __init__(self, **kwargs):
        super(iu, self).__init__(**kwargs)
        self.orientation = "vertical"

        #isso serve para a class ui conseguir se comunicar com as outra class 
        self.Grid = Grid()
        self.scroll = Scroll(self.Grid)
        #self.hotbar = HotBar()

        #adicionando os widget principais ao iu
        self.add_widget(self.scroll)
        #self.add_widget(self.hotbar) #adiciona o widget uma "barra de ferramenas" ao layout
        
        #self.children[0].on_release = self.Grid.adicionar #<- altera o acomportamento de um widget filho # **não vou usar esse jeito por ser hororoso e claramente fragio**


class Scroll(ScrollView):# <- ele deve conter o widget pelo que vai percorrer, ele so pode conter um unico widget
    def __init__(self, Grid, **kwargs):
        super().__init__(**kwargs)

        # inicio de caracteristicas
        # ver o arquivo my.kv: <Scroll>
        # fim de caracteristicas

        self.add_widget(Grid) # <- o unico widget que pode conter e vai percorrer





class Grid(FloatLayout): # <- tabuleiro  
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.size_hint = (None, None) # <- desativa o tamanho automatico com base nos widget filhos
        self.size = (10000,10000) # <- define o tamanho do layout

        with self.canvas as canva: #adicionar um quadriculado de findo
            for i in range(0,101):
                Line(points = [self.size[0]/100 * i, self.size[1], self.size[0]/100 * i, 0])# linha vertiicais
                Line(points = [self.size[0], self.size[1]/100 * i, 0, self.size[1]/100 * i])#linhas horisontais


    def adicionar(self, *args):
        self.add_widget(Button(
                                text = "p"*randint(1,10),
                                size_hint = (None, None), # <- desativa o tamanho relativo ao "pai"
                                size = (randint (20, 100), randint(20,100)), # <- altera o tamanho para um numero aleatorio
                                pos = (randint(1,self.size[0]), randint(1, self.size[1] )) # <- altera a posicão para um numero aleatorio
                                )
                        )
    #fim função 'adicionar'


        
class MyApp(App):
    def build(self):

        Window.size = (1000,750)# <- define o tamanho da janela 

        return iu()

MyApp().run()