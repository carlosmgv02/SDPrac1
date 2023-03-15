

class Direccion:
    def __init__(self, calle, piso):
        self.calle = calle
        self.piso = piso

    def __str__(self):
        return f"Calle: {self.calle}, piso: {self.piso}"