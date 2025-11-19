import os 
class Menu:

    def mostrarMenu(self):
        print("=== Cálculo de Triángulos ===")
        print("1. Calcular lado usando el Teorema del Seno")
        print("2. Calcular angulo usando el Teorema del Seno")
        print("3. Calcular angulo usando el Teorema del Coseno")
        print("4. Calcular lado usando el Teorema del Coseno")
        print("5. Salir")
        obtenerOpcion = self.obtenerOpcion()

    def obtenerOpcion(self):
        funciones = {"1": self.ladoSeno}
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
        return lado_opuesto, angulo_opuesto, angulo_conocido