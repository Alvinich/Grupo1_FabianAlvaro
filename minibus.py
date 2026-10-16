"""Clase derivada Minibus."""
from vehiculo import Vehiculo


class Minibus(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, numero_viajes, costo_por_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        self.numero_viajes = numero_viajes
        self.costo_por_km = costo_por_km

    @property
    def numero_viajes(self):
        return self.__numero_viajes

    @numero_viajes.setter
    def numero_viajes(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El número de viajes debe ser un entero no negativo.")
        self.__numero_viajes = valor

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
        return (f"[Minibús] {base} | Viajes: {self.numero_viajes} | "
                f"Costo/km: Bs {self.costo_por_km:.2f}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self.costo_por_km
