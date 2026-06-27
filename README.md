# Sistema Básico de Gestión de Restaurante

## Estudiante

**Nombre:** Elkin Esteban Tovar Caicedo

## Descripción del sistema

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite registrar productos y clientes, almacenarlos en listas y mostrar la información registrada en la consola.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

- **producto.py:** contiene la clase `Producto`.
- **cliente.py:** contiene la clase `Cliente`.
- **restaurante.py:** contiene la clase `Restaurante`, que administra los productos y clientes.
- **main.py:** crea los objetos y muestra la información en consola.

## Tipos de datos utilizados

- **str:** nombres y teléfono.
- **int:** edad y cantidad.
- **float:** precio de los productos.
- **bool:** disponibilidad de productos y clientes frecuentes.
- **list:** almacenamiento de productos y clientes.

## Reflexión

Utilizar identificadores descriptivos hace que el código sea más fácil de entender y mantener. Además, emplear tipos de datos adecuados y listas permite organizar mejor la información y desarrollar proyectos de forma más ordenada utilizando Programación Orientada a Objetos.
