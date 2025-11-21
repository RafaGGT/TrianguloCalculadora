import math


class Triangulo:
    def __init__(self):
        pass
     
    def _validar_lado(self, valor, nombre):
        if valor is None or valor <= 0:
            raise ValueError(f"El lado {nombre} debe ser mayor que cero.")

    def _validar_angulo(self, valor, nombre):
        if valor is None or valor <= 0 or valor >= 180:
            raise ValueError(f"El ángulo {nombre} debe estar entre 0 y 180 grados (exclusivo).")

    def teorema_seno_lado(self, lado_opuesto, angulo_opuesto, angulo_conocido):
        self._validar_lado(lado_opuesto, "opuesto")
        self._validar_angulo(angulo_opuesto, "opuesto")
        self._validar_angulo(angulo_conocido, "conocido")
        # Convertir ángulos a radianes o grados según sea necesario
        angulo_opuesto_rad = math.radians(angulo_opuesto)
        angulo_conocido_rad = math.radians(angulo_conocido)
        # Evitar división por cero si el seno del ángulo opuesto es cero
        denom = math.sin(angulo_opuesto_rad)
        if math.isclose(denom, 0.0, abs_tol=1e-9):
            raise ValueError("El ángulo opuesto no puede tener seno igual a cero.")
        return (lado_opuesto * math.sin(angulo_conocido_rad)) / denom

    def teorema_seno_angulo(self, lado_opuesto, angulo_opuesto, lado_conocido):
        self._validar_lado(lado_opuesto, "opuesto")
        self._validar_lado(lado_conocido, "conocido")
        self._validar_angulo(angulo_opuesto, "opuesto")
        angulo_opuesto_rad = math.radians(angulo_opuesto)
        razon = (lado_conocido * math.sin(angulo_opuesto_rad)) / lado_opuesto
        if not -1.0 <= razon <= 1.0:
            raise ValueError("Los datos no producen un ángulo real (|razón| > 1).")
        angulo_conocido_rad = math.asin(razon)
        return math.degrees(angulo_conocido_rad)

    def teorema_coseno_angulo(self, lado_a, lado_b, lado_c):
        # Validar lados
        self._validar_lado(lado_a, "a")
        self._validar_lado(lado_b, "b")
        self._validar_lado(lado_c, "c")
        # Calcular el ángulo C usando la ley del coseno
        divisor = 2 * lado_a * lado_b
        if math.isclose(divisor, 0.0, abs_tol=1e-12):
            raise ValueError("Los lados a y b deben ser distintos de cero.")
        cos_valor = (lado_a**2 + lado_b**2 - lado_c**2) / divisor
        if cos_valor < -1.0 or cos_valor > 1.0:
            raise ValueError("Los datos no producen un ángulo real (coseno fuera de rango).")
        angulo_C_rad = math.acos(cos_valor)
        return math.degrees(angulo_C_rad)

    def teorema_coseno_lado(self, lado_a, lado_b, angulo_C):
        # Validar lados y ángulo
        self._validar_lado(lado_a, "a")
        self._validar_lado(lado_b, "b")
        self._validar_angulo(angulo_C, "C")
        angulo_C_rad = math.radians(angulo_C)
        valor = lado_a**2 + lado_b**2 - 2 * lado_a * lado_b * math.cos(angulo_C_rad)
        if valor < 0:
            raise ValueError("Los datos no generan un lado real (resultado negativo bajo la raíz).")
        return math.sqrt(valor)