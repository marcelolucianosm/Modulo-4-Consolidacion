#diccionario = [{'x': 2,   'y': 1,  'z': 4}, 
#      {'x': 'a',   'y': 'b', 'z': 'c'},
#      {'x': 22,  'y': 10, 'z': 40},
#      {'x': 132, 'y': 89, 'z': 1}]
diccionario =[{'marca': 'Toyota', 'modelo': 'Yaris', 'numero_ruedas': 4, 'velocidad': 160, 'cilindrada': 1500}]
headers = ['marca','modelo','numero_ruedas','velocidad','cilindrada']
largo = headers.__len__()
contador=0
datos = []
for row, _dict in enumerate(diccionario):
    for col, key in enumerate(headers):
        contador+=1
        datos.append(_dict[key])
        if contador==largo:
            print(datos)
            contador=0
            datos = []
