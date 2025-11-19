from vista.menu import Menu
from modelo.Triangulo import Triangulo
from controlador.TrianguloController import Controller


vista = Menu()
modelo = Triangulo()
controlador = Controller(vista, modelo)

datos = vista.mostrarMenu()
controlador.calcular_lado_seno()
