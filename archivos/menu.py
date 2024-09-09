import uuid
import os
import platform
import time
 
delay = 2
 
class Animal:
    def __init__(self, nombre, raza, especie):
        self.id  = str(uuid.uuid4())[0:8]
        self.nombre = nombre
        self.raza = raza
        self.especie = especie

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Especie: {self.especie}"

    def leer_animales():
        print("Se está leyendo el archivo animales.csv")
        time.sleep(delay)

    def registrar_animal():
        print("Se procede a registrar un animal.")
        time.sleep(delay)

    def salir():
        print("Gracias por utilizar el sistema.")
    
    def f_repetir():
        opcion = input("Si desea volver al menú ingrese [s], de lo contrario, presione cualquier tecla: ")    
        if opcion.lower() == "s":
            limpiar_consola()
    
            return True
        else:
            limpiar_consola()
        return False
    
    def limpiar_consola():
        sistema = platform.system()

        if sistema == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def menu():
        print("Menú...")
        print("1.- Leer Animales.")
        print("2.- Registrar un nuevo animal.")
        opcion = input("Ingrese la opción: [1, 2]: ")
        limpiar_consola()
        
        if opcion == "1":
            leer_animales()
            limpiar_consola()
        elif opcion == "2":
            registrar_animal()
            limpiar_consola()
        else:
            print("Opción inválida.")
            time.sleep(delay)
            limpiar_consola()

    def main():
        repetir = True
        while repetir:
            menu()
            repetir = f_repetir()
        
        salir()

main()