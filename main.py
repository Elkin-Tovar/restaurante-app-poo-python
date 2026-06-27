# Programa principal.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el restaurante.
mi_restaurante = Restaurante("Restaurante El Buen Sabor")


# Crear productos.
producto1 = Producto("Hamburguesa", 6.50, 15, True)
producto2 = Producto("Pizza Familiar", 12.00, 8, True)


# Crear clientes.
cliente1 = Cliente("Juan Pérez", 22, "0991111111", True)
cliente2 = Cliente("María Gómez", 30, "0982222222", False)


# Agregar productos al restaurante.
mi_restaurante.agregar_producto(producto1)
mi_restaurante.agregar_producto(producto2)


# Agregar clientes al restaurante.
mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)


# Mostrar la información registrada.
print("=" * 40)
print(mi_restaurante.nombre)
print("=" * 40)

mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()