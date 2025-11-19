from modelo.Triangulo import Triangulo as tri
import os 
class Menu:

    def mostrarMenu(self):
        print("=== Cálculo de Triángulos ===")
        print("1. Calcular lado usando el Teorema del Seno")
        print("2. Calcular angulo usando el Teorema del Seno")
        print("3. Calcular angulo usando el Teorema del Coseno")
        print("4. Calcular lado usando el Teorema del Coseno")
        print("5. Salir")
        return self.obtenerOpcion()   


    def obtenerOpcion(self):
        funciones = {
            "1": self.ladoSeno, 
            "2": self.anguloSeno}
        opcion = input("Seleccione una opción (1-5): ")
        if opcion in funciones:
            return funciones[opcion]()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            return self.obtenerOpcion()

    def ladoSeno(self):
        lado_opuesto = float(input("Ingrese el lado opuesto conocido: "))
        angulo_opuesto = float(input("Ingrese el ángulo opuesto conocido (en grados): "))
        angulo_conocido = float(input("Ingrese el ángulo conocido (en grados): "))
        resultado = tri().teorema_seno_lado(lado_opuesto, angulo_opuesto, angulo_conocido)
        print("\nTu ecuación:")
        print(f"x / sin({angulo_conocido}°) = {lado_opuesto} / sin({angulo_opuesto}°)\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()

    def anguloSeno(self):
        lado_opuesto = float(input("Ingrese el lado opuesto conocido: "))
        angulo_opuesto = float(input("Ingrese el ángulo opuesto conocido (en grados): "))
        lado_conocido = float(input("Ingrese el lado conocido: "))
        resultado = tri().teorema_seno_angulo(lado_opuesto, angulo_opuesto, lado_conocido)
        print("\nTu ecuación:")
        print(f" {lado_conocido} / sin(x°) = sin({angulo_opuesto}°) / {lado_opuesto}\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()