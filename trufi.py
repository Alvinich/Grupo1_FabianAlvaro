"""Clase derivada Trufi."""
from vehiculo import Vehiculo


class Trufi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, numero_rutas, costo_por_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        self.numero_rutas = numero_rutas
        self.costo_por_km = costo_por_km

    @property
    def numero_rutas(self):
        return self.__numero_rutas

    @numero_rutas.setter
    def numero_rutas(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El número de rutas debe ser un entero no negativo.")
        self.__numero_rutas = valor

    @property
    def costo_por_km(self):
        return self.__costo_por_km

    @costo_por_km.setter
    def costo_por_km(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El costo por kilómetro debe ser mayor que cero.")
        self.__costo_por_km = float(valor)

    def mostrar_informacion(self):
        base = super().mostrar_informacion()
        return (f"[Trufi] {base} | Rutas: {self.numero_rutas} | "
                f"Costo/km: Bs {self.costo_por_km:.2f}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self.costo_por_km
