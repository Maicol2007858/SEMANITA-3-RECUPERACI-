class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\n🐾 INFORMACIÓN DE LA MASCOTA")
        print("----------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau Guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido desconocido.")