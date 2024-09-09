from clases import Automovil
import csv


def imprimir(objeto,datos):
    print("********************************************************************************************************************************************************************")
    print(f"{objeto} {datos}")
    print("********************************************************************************************************************************************************************")
    
##### implementar modo "x" para que generre error y usar  try  except
    
def guardar(archivo,informacion):
    informacion2 = str(informacion)
    informacion2 += "\n"
    with open(archivo, 'a') as fichero:
        fichero.write(informacion2)
        fichero.close()
        
def guardar_encabezado(archivo,encabezados):
    with open(archivo, 'a') as fichero:
      fichero.write(str(encabezados))
      fichero.close()

    

def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos

def obtenerEncabezados(encabezados):
    titulos = ""
    for detalle in encabezados:
        detalle+=","
        titulos += detalle
    titulos += "\n"
    
    return titulos

def obtenerListaEncabezados(encabezados):
    lista_encabezado = []
    for detalle_encabezado in encabezados:
        lista_encabezado.append(detalle_encabezado)
       
    return lista_encabezado

def datos_de_diccionario(diccionario,encabezados):
    
    #diccionario=[{'marca': 'Toyota', 'modelo': 'Yaris', 'numero_ruedas': 4, 'velocidad': 160, 'cilindrada': 1500}]
    diccionario2 = dict=[diccionario]
    contador=0
    datos = []
    largo=encabezados.__len__()
    for row, _dict in enumerate(diccionario2):
        for col, key in enumerate(encabezados):
            contador+=1
            datos.append(_dict[key])
            if contador==largo:
                #print(datos)
                contador=0
                #datos = []
    #return datos
    datos_str = str(datos)
    cadena1       = datos_str.replace("[", "")
    datos_finales = cadena1.replace("]", "")
    
    return datos_finales