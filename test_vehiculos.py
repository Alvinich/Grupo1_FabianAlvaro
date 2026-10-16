import unittest

from trufi import Trufi
from minibus import Minibus
from radiotaxi import Radiotaxi
from vehiculo import Vehiculo


class PruebasTransporte(unittest.TestCase):
    def setUp(self):
        self.flota = [
            Trufi("T-01", "Toyota", 15, 100, 3, 2.5),
            Minibus("M-01", "Nissan", 25, 200, 4, 3.0),
            Radiotaxi("R-01", "Suzuki", 4, 50, "Zona Sur", 4.0),
        ]

    def test_registro_trufi(self):
        self.assertEqual(self.flota[0].codigo, "T-01")

    def test_registro_minibus(self):
        self.assertEqual(self.flota[1].numero_viajes, 4)

    def test_registro_radiotaxi(self):
        self.assertEqual(self.flota[2].area_asignada, "Zona Sur")

    def test_herencia(self):
        for v in self.flota:
            self.assertIsInstance(v, Vehiculo)
            self.assertIn(v.codigo, v.mostrar_informacion())

    def test_polimorfismo(self):
        costos = [v.calcular_costo_operativo() for v in self.flota]
        self.assertEqual(costos, [250.0, 600.0, 200.0])

    def test_validacion_kilometraje_negativo(self):
        with self.assertRaises(ValueError):
            Trufi("T-02", "Toyota", 15, -10, 3, 2.5)

    def test_validacion_capacidad_negativa(self):
        with self.assertRaises(ValueError):
            Minibus("M-02", "Nissan", -1, 10, 3, 2.5)

    def test_validacion_costo_invalido(self):
        with self.assertRaises(ValueError):
            Radiotaxi("R-02", "Suzuki", 4, 10, "Centro", 0)

    def test_costo_total(self):
        total = sum(v.calcular_costo_operativo() for v in self.flota)
        self.assertEqual(total, 1050.0)

    def test_clase_base_abstracta(self):
        with self.assertRaises(TypeError):
            Vehiculo("X", "Y", 1, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
