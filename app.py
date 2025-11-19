from vista.menu import Menu
from modelo.Triangulo import Triangulo
from controlador.TrianguloController import Controller



vista = Menu()
modelo = Triangulo()
controlador = Controller(vista, modelo)

# EL MENU PIDE DATOS
lado_opuesto, angulo_opuesto, angulo_conocido = vista.mostrarMenu()

# EL CONTROLADOR CALCULA
controlador.calcular_lado_seno(lado_opuesto, angulo_opuesto, angulo_conocido)
