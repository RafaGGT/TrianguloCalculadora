from modelo.Triangulo import Triangulo as tri


class Menu:
    def __init__(self):
        self.triangulo = tri()

    def mostrarMenu(self):
        funciones = {
            "1": self.ladoSeno,
            "2": self.anguloSeno,
            "3": self.anguloCoseno,
            "4": self.ladoCoseno,
            "5": self.salir,
        }
        while True:
            print("=== Cálculo de Triángulos ===")
            print("1. Calcular lado usando el Teorema del Seno")
            print("2. Calcular ángulo usando el Teorema del Seno")
            print("3. Calcular ángulo usando el Teorema del Coseno")
            print("4. Calcular lado usando el Teorema del Coseno")
            print("5. Salir")
            opcion = input("Seleccione una opción (1-5): ")
            accion = funciones.get(opcion)
            if accion is None:
                print("Opción no válida. Por favor, intente de nuevo.\n")
                continue
            if accion():
                break

    def solicitar_float(self, mensaje, minimo=None, maximo=None):
        while True:
            try:
                valor = float(input(mensaje))
            except ValueError:
                print("Entrada inválida. Intente nuevamente con un número.\n")
                continue
            if minimo is not None and valor <= minimo:
                print(f"El valor debe ser mayor que {minimo}.\n")
                continue
            if maximo is not None and valor >= maximo:
                print(f"El valor debe ser menor que {maximo}.\n")
                continue
            return valor

    def ladoSeno(self):
        lado_opuesto = self.solicitar_float("Ingrese el lado opuesto conocido: ", minimo=0)
        angulo_opuesto = self.solicitar_float(
            "Ingrese el ángulo opuesto conocido (en grados): ", minimo=0, maximo=180
        )
        angulo_conocido = self.solicitar_float(
            "Ingrese el ángulo conocido (en grados): ", minimo=0, maximo=180
        )
        try:
            resultado = self.triangulo.teorema_seno_lado(
                lado_opuesto, angulo_opuesto, angulo_conocido
            )
        except ValueError as error:
            print(f"Error: {error}\n")
            return False
        print("\nTu ecuación:")
        print(f"x / sin({angulo_conocido}°) = {lado_opuesto} / sin({angulo_opuesto}°)\n")
        print(f"Resultado: {resultado}\n")
        return False

    def anguloSeno(self):
        lado_opuesto = self.solicitar_float("Ingrese el lado opuesto conocido: ", minimo=0)
        angulo_opuesto = self.solicitar_float(
            "Ingrese el ángulo opuesto conocido (en grados): ", minimo=0, maximo=180
        )
        lado_conocido = self.solicitar_float("Ingrese el lado conocido: ", minimo=0)
        try:
            resultado = self.triangulo.teorema_seno_angulo(
                lado_opuesto, angulo_opuesto, lado_conocido
            )
        except ValueError as error:
            print(f"Error: {error}\n")
            return False
        print("\nTu ecuación:")
        print(f"{lado_conocido} / sin(x°) = sin({angulo_opuesto}°) / {lado_opuesto}\n")
        print(f"Resultado: {resultado}\n")
        return False

    def anguloCoseno(self):
        lado_a = self.solicitar_float("Ingrese el lado a: ", minimo=0)
        lado_b = self.solicitar_float("Ingrese el lado b: ", minimo=0)
        lado_c = self.solicitar_float("Ingrese el lado opuesto al ángulo buscado (c): ", minimo=0)
        try:
            resultado = self.triangulo.teorema_coseno_angulo(lado_a, lado_b, lado_c)
        except ValueError as error:
            print(f"Error: {error}\n")
            return False
        print("\nTu ecuación:")
        print(f"cos(C) = ({lado_a}^2 + {lado_b}^2 - {lado_c}^2) / (2 * {lado_a} * {lado_b})\n")
        print(f"Resultado: {resultado}\n")
        return False

    def ladoCoseno(self):
        lado_a = self.solicitar_float("Ingrese el lado a: ", minimo=0)
        lado_b = self.solicitar_float("Ingrese el lado b: ", minimo=0)
        angulo_C = self.solicitar_float(
            "Ingrese el ángulo incluido (en grados): ", minimo=0, maximo=180
        )
        try:
            resultado = self.triangulo.teorema_coseno_lado(lado_a, lado_b, angulo_C)
        except ValueError as error:
            print(f"Error: {error}\n")
            return False
        print("\nTu ecuación:")
        print(
            f"c^2 = {lado_a}^2 + {lado_b}^2 - 2 * {lado_a} * {lado_b} * cos({angulo_C}°)\n"
        )
        print(f"Resultado: {resultado}\n")
        return False

    def salir(self):
        print("Hasta luego.")
        return True
