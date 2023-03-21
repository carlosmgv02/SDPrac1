

class Persona:
    def __init__(self, nombre, edad, direccion, telefono, email):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Correo: {self.email}"
