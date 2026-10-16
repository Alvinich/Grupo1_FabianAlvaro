"""Clase base Vehiculo del sistema de transporte universitario."""
from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase base con los atributos comunes a todos los vehículos."""

    def __init__(self, codigo, marca, capacidad, kilometraje):
        self.codigo = codigo
        self.marca = marca
        self.capacidad = capacidad
        self.kilometraje = kilometraje

    # --- Encapsulamiento: atributos privados con validación ---
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El código del vehículo no puede estar vacío.")
        self.__codigo = valor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = valor

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La capacidad debe ser un entero no negativo.")
        self.__capacidad = valor

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self.__kilometraje = float(valor)

    # --- Comportamiento común (reutilizado por las clases derivadas) ---
    def mostrar_informacion(self):
        return (f"Código: {self.codigo} | Marca: {self.marca} | "
                f"Capacidad: {self.capacidad} pasajeros | "
                f"Kilometraje: {self.kilometraje:.1f} km")

    @abstractmethod
    def calcular_costo_operativo(self):
        """Método polimórfico: cada tipo de vehículo lo implementa a su manera."""

    def __str__(self):
        return self.mostrar_informacion()
