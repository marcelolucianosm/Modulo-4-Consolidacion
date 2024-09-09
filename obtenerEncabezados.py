


def obtenerEncabezados(encabezados):
    titulos = ""
    for detalle in encabezados:
        detalle+=";"
        titulos += detalle
    titulos += "\n"
    
    return titulos