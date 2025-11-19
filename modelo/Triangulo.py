import math

class Triangulo:
    def __init__(self, lado_a=None, lado_b=None, lado_c=None, 
                 angulo_A=None, angulo_B=None, angulo_C=None):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        self.angulo_A = angulo_A
        self.angulo_B = angulo_B
        self.angulo_C = angulo_C

    def teorema_seno_lado(self, lado_opuesto, angulo_opuesto, angulo_conocido):
        angulo_opuesto_rad = math.radians(angulo_opuesto)
        angulo_conocido_rad = math.radians(angulo_conocido)
        return (lado_opuesto * math.sin(angulo_conocido_rad)) / math.sin(angulo_opuesto_rad)

    def teorema_seno_angulo(self, lado_opuesto, angulo_opuesto, lado_conocido):
        angulo_opuesto_rad = math.radians(angulo_opuesto)
        angulo_conocido_rad = math.asin((lado_conocido * math.sin(angulo_opuesto_rad)) / lado_opuesto)
        return math.degrees(angulo_conocido_rad)

    def teorema_coseno_angulo(self, lado_a, lado_b, lado_c):
        angulo_C_rad = math.acos((lado_a**2 + lado_b**2 - lado_c**2) / (2 * lado_a * lado_b))
        return math.degrees(angulo_C_rad)

    def teorema_coseno_lado(self, lado_a, lado_b, angulo_C):
        angulo_C_rad = math.radians(angulo_C)
        return math.sqrt(lado_a**2 + lado_b**2 - 2 * lado_a * lado_b * math.cos(angulo_C_rad))
