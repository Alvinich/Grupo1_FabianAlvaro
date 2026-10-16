"""Sistema de gestión de transporte universitario (menú de consola)."""
from trufi import Trufi
from minibus import Minibus
from radiotaxi import Radiotaxi
from vehiculo import Vehiculo


def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  Error: el dato no puede estar vacío.")


def leer_entero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  Error: ingrese un número entero válido.")
            continue
        if valor < minimo:
            print(f"  Error: el valor debe ser mayor o igual que {minimo}.")
            continue
        return valor


def leer_decimal(mensaje, minimo=0.0, estricto=False):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("  Error: ingrese un número válido.")
            continue
        if valor < minimo or (estricto and valor == minimo):
            print("  Error: el sistema rechaza el dato (valor negativo o no válido).")
            continue
        return valor


def datos_comunes():
    codigo = leer_texto("Código: ")
    marca = leer_texto("Marca: ")
    capacidad = leer_entero("Capacidad de pasajeros: ")
    km = leer_decimal("Kilometraje recorrido: ")
    return codigo, marca, capacidad, km


def registrar_trufi(flota):
    codigo, marca, cap, km = datos_comunes()
    rutas = leer_entero("Número de rutas: ")
    costo = leer_decimal("Costo por km (Bs): ", estricto=True)
    flota.append(Trufi(codigo, marca, cap, km, rutas, costo))
    print("  Trufi registrado correctamente.")


def registrar_minibus(flota):
    codigo, marca, cap, km = datos_comunes()
    viajes = leer_entero("Número de viajes: ")
    costo = leer_decimal("Costo por km (Bs): ", estricto=True)
    flota.append(Minibus(codigo, marca, cap, km, viajes, costo))
    print("  Minibús registrado correctamente.")


def registrar_radiotaxi(flota):
    codigo, marca, cap, km = datos_comunes()
    area = leer_texto("Área asignada: ")
    costo = leer_decimal("Costo por km (Bs): ", estricto=True)
    flota.append(Radiotaxi(codigo, marca, cap, km, area, costo))
    print("  Radiotaxi registrado correctamente.")


def mostrar_vehiculos(flota):
    if not flota:
        print("  No hay vehículos registrados.")
        return
    for v in flota:
        print("  " + v.mostrar_informacion())


def calcular_costos(flota):
    if not flota:
        print("  No hay vehículos registrados.")
        return
    # Polimorfismo: misma llamada, cada objeto ejecuta su propia implementación.
    for v in flota:
        print(f"  {v.codigo} ({type(v).__name__}): Bs {v.calcular_costo_operativo():.2f}")


def costo_total(flota):
    total = sum(v.calcular_costo_operativo() for v in flota)
    print(f"  Costo operativo total: Bs {total:.2f}")


MENU = """
===== TRANSPORTE UNIVERSITARIO =====
1. Registrar un trufi
2. Registrar un minibús
3. Registrar un radiotaxi
4. Mostrar los vehículos registrados
5. Calcular el costo operativo de cada vehículo
6. Calcular el costo operativo total
7. Salir
"""


def main():
    flota: list[Vehiculo] = []
    acciones = {
        "1": registrar_trufi, "2": registrar_minibus, "3": registrar_radiotaxi,
        "4": mostrar_vehiculos, "5": calcular_costos, "6": costo_total,
    }
    while True:
        print(MENU)
        try:
            opcion = input("Seleccione una opción: ").strip()
        except EOFError:
            break
        if opcion == "7":
            print("Hasta luego.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("  Opción no válida.")
            continue
        accion(flota)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado.")
