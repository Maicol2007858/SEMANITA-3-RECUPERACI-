# Programa de gestión de mascotas - Programación Tradicional

# Función para registrar mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad


# Función para mostrar información
def mostrar_mascota(nombre, especie, edad):
    print("\n🐾 INFORMACIÓN DE LA MASCOTA")
    print("----------------------------")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")


# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)