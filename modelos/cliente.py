# Clase que representa a un cliente.

class Cliente:

    def __init__(self, nombre: str, edad: int, telefono: str, cliente_frecuente: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        frecuente = "Sí" if self.cliente_frecuente else "No"

        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} | "
            f"Teléfono: {self.telefono} | "
            f"Cliente frecuente: {frecuente}"
        )