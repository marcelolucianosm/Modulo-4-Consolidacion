from clases import Vehiculo, Automovil, AutomovilCarga, AutomovilPasajeros, Bicicleta, Motocicleta
from utilitarios import imprimir,guardar,recuperar,guardar_encabezado,obtenerEncabezados,datos_de_diccionario,obtenerListaEncabezados

vehiculo1 = Vehiculo("Toyota","Yaris",4)
datos = str(vehiculo1.Ver())
imprimir(" Vehiculo1 :",datos)

automovil1 = Automovil("Toyota","Yaris",4, 160 , 1500)
datos = str(automovil1.Ver())
imprimir(" Automovil1 :", datos)

automovilPasajeros1 = AutomovilPasajeros("Ford","Fiesta",4, 180 , 1800,6)
datos = str(automovilPasajeros1.Ver())
imprimir(" AutomovilPasajeros1 :", datos)

automovilCarga1 = AutomovilCarga("Chevrolet","Dmax",4, 180 , 2500, 1000)
datos = str(automovilCarga1.Ver())
imprimir(" AutomovilCarga1 :", datos)

bicicleta1 = Bicicleta("Bianchi","Spider",2 ,"Carrera")
datos = str(bicicleta1.Ver())
imprimir(" Bicicleta1 :", datos)

motocicleta1 = Motocicleta("BMW","1200R",2 ,"OFFROAD", 21 ,"DobleT","4T")
datos = str(motocicleta1.Ver())
imprimir(" Motocicleta1 :",datos)

datos = " Motocicleta es Instancia con relacion a Vehiculo ",isinstance(motocicleta1,Vehiculo)
imprimir(" Clase Vehiculo :",datos)

datos = " Motocicleta es Instancia con relacion a Automovil ",isinstance(motocicleta1,Automovil)
imprimir(" Clase Automovil :",datos)

datos = " Motocicleta es Instancia con relacion a AutomovilPasajeros ",isinstance(motocicleta1,AutomovilPasajeros)
imprimir(" Clase AutomovilPasajeros :",datos)

datos = " Motocicleta es Instancia con relacion a AutomovilCarga ",isinstance(motocicleta1,AutomovilCarga)
imprimir(" Clase AutomovilCarga :",datos)

datos = " Motocicleta es Instancia con relacion a Bicicleta ",isinstance(motocicleta1,Bicicleta)
imprimir(" Clase Bicicleta :",datos)

datos = " Motocicleta es Instancia con relacion a Motocicleta ",isinstance(motocicleta1,Motocicleta)
imprimir(" Clase Motocicleta :",datos)

####################################################################################################
guardar_encabezado("vehiculos.csv",obtenerEncabezados(automovil1.__dict__.keys()))

lista_encabezados = obtenerListaEncabezados(automovil1.__dict__.keys())

datos_imprimir = datos_de_diccionario(automovil1.__dict__,lista_encabezados)

guardar("vehiculos.csv",datos_imprimir)

automoviles = recuperar("vehiculos.csv")

for automovil in automoviles:
    imprimir('',automovil)
    #imprimir(" Archivo CSV : ",automovil)

