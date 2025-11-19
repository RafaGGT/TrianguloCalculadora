class Controller:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def calcular_lado_seno(self):
        lado_opuesto, angulo_opuesto, angulo_conocido = self.vista.mostrarMenu()
        resultado = self.modelo.teorema_seno_lado(lado_opuesto, angulo_opuesto, angulo_conocido)

        print(f"\nTu ecuación:")
        print(f"x / sin({angulo_conocido}°) = {lado_opuesto} / sin({angulo_opuesto}°)")
        print(f"Resultado: {resultado}\n")
