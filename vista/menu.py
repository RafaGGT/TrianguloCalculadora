from modelo.Triangulo import Triangulo as tri
import os 
class Menu:

    def mostrarMenu(self):
        os.system("cls")
        print("=== Cálculo de Triángulos ===")
        print("1. Calcular lado usando el Teorema del Seno")
        print("2. Calcular angulo usando el Teorema del Seno")
        print("3. Calcular lado usando el Teorema del Coseno")
        print("4. Calcular angulo usando el Teorema del Coseno")
        print("5. Salir")
        return self.obtenerOpcion()   

    def salir(self):
        print("Saliendo del programa. ¡Hasta luego!")
        return

    def obtenerOpcion(self):
        funciones = {
            "1": self.ladoSeno, 
            "2": self.anguloSeno,
            "3": self.ladoCoseno,
            "4": self.anguloCoseno}
        opcion = input("Seleccione una opción (1-5): ")
        if opcion in funciones:
            return funciones[opcion]()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            return self.obtenerOpcion()

    def ladoSeno(self):
        print("\nUsando el Teorema del Seno para calcular un lado:")
        print("X/sin(A°) =  B/sin(B°)\n")
        try:
            lado_opuesto = float(input("Ingrese el lado B: "))
            angulo_opuesto = float(input("Ingrese el ángulo B: "))
            angulo_conocido = float(input("Ingrese el ángulo A: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")
            return self.ladoSeno()
        resultado = tri().teorema_seno_lado(lado_opuesto, angulo_opuesto, angulo_conocido)
        print("\nTu ecuación:")
        print(f"x / sin({angulo_conocido}°) = {lado_opuesto} / sin({angulo_opuesto}°)\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()

    def anguloSeno(self):
        print("\nUsando el Teorema del Seno para calcular un ángulo:")
        print("A/sin(X°) =  B/sin(B°)\n")
        try: 
            lado_opuesto = float(input("Ingrese el lado B: "))
            angulo_opuesto = float(input("Ingrese el ángulo B: "))
            lado_conocido = float(input("Ingrese el lado A: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")
            return self.anguloSeno()
        resultado = tri().teorema_seno_angulo(lado_opuesto, angulo_opuesto, lado_conocido)
        print("\nTu ecuación:")
        print(f" {lado_conocido} / sin(x°) = {lado_opuesto} / sin({angulo_opuesto}°)\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()

    def ladoCoseno(self):
        print("\nUsando el Teorema del Coseno para calcular un lado:")
        print("x² = a² + b² - 2ab * cos(C°)\n")
        try:
            lado_a = float(input("Ingrese el lado a conocido: "))
            lado_b = float(input("Ingrese el lado b conocido: "))
            angulo_C = float(input("Ingrese el ángulo C: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")
            return self.ladoCoseno()
        resultado = tri().teorema_coseno_lado(lado_a, lado_b, angulo_C)
        print("\nTu ecuación:")
        print(f"x² = {lado_a}² + {lado_b}² - 2 * {lado_a} * {lado_b} * cos({angulo_C}°)\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()

    def anguloCoseno(self):
        print("\nUsando el Teorema del Coseno para calcular un ángulo:")
        print("cos(x°) = (a² + b² - c²) / (2ab)\n")
        try:
            lado_a = float(input("Ingrese el lado a conocido: "))
            lado_b = float(input("Ingrese el lado b conocido: "))
            lado_c = float(input("Ingrese el lado c conocido: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")
            return self.anguloCoseno()
        resultado = tri().teorema_coseno_angulo(lado_a, lado_b, lado_c)
        print("\nTu ecuación:")
        print(f"cos(x°) = ({lado_a}² + {lado_b}² - {lado_c}²) / (2 * {lado_a} * {lado_b})\n")
        print(f"Resultado: {resultado}\n")
        return self.obtenerOpcion()