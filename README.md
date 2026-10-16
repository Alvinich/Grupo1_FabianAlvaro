# Sistema de Gestión de Transporte Universitario

Proyecto grupal de **PFU-111 Programación Fundamental** (Semana 11, Grupo 1).
Tema 7: Programación Orientada a Objetos — herencia y polimorfismo, en Python.

## Descripción

Programa de consola que registra vehículos de transporte universitario
(trufis, minibuses y radiotaxis), muestra sus características y calcula su
costo operativo. Todos los vehículos heredan de la clase base `Vehiculo` y se
gestionan en una misma lista; el método `calcular_costo_operativo()` se invoca
de forma polimórfica, sin cadenas de condiciones.

## Estructura

```
transporte-universitario/
├── vehiculo.py          # Clase base abstracta Vehiculo
├── trufi.py             # Trufi(Vehiculo)
├── minibus.py           # Minibus(Vehiculo)
├── radiotaxi.py         # Radiotaxi(Vehiculo)
├── main.py              # Menú de consola
├── test_vehiculos.py    # Pruebas automáticas (unittest)
├── docs/Informe_PFU-111_Proyecto_Transporte.pdf
└── README.md
```

## Modelo de clases

| Clase | Atributos propios | Regla de costo operativo |
|-------|-------------------|--------------------------|
| `Vehiculo` (base) | código, marca, capacidad, kilometraje | método abstracto |
| `Trufi` | número de rutas, costo por km | km × costo por km |
| `Minibus` | número de viajes, costo por km | km × costo por km |
| `Radiotaxi` | área asignada, costo por km | km × costo por km |

## Requisitos y ejecución

Requiere Python 3.9 o superior (sin dependencias externas).

```bash
git clone <URL-DEL-REPOSITORIO>
cd transporte-universitario
python main.py                 # ejecutar el programa
python -m unittest -v          # ejecutar las pruebas
```

## Validaciones

Capacidad y kilometraje no pueden ser negativos; el costo por kilómetro debe
ser mayor que cero; código, marca y área no pueden estar vacíos. Los errores
de entrada en el menú se rechazan y se vuelve a pedir el dato.

## Integrantes

- Integrante 1: _nombre_ — diseño del diagrama y clase base `Vehiculo`
- Integrante 2: _nombre_ — implementación de `Trufi`
- Integrante 3: _nombre_ — implementación de `Minibus`
- Integrante 4: _nombre_ — implementación de `Radiotaxi`, integración y pruebas
