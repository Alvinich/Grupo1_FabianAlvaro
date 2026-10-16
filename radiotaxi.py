"""Clase derivada Radiotaxi."""
from vehiculo import Vehiculo


class Radiotaxi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, area_asignada, costo_por_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        self.area_asignada = area_asignada
        self.costo_por_km = costo_por_km

    @property
    def area_asignada(self):
        return self.__area_asignada

    @area_asignada.setter
    def area_asignada(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El área asignada no puede estar vacía.")
        self.__area_asignada = valor

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
        return (f"[Radiotaxi] {base} | Área: {self.area_asignada} | "
                f"Costo/km: Bs {self.costo_por_km:.2f}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self.costo_por_km
