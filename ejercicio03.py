def contar_palabras(cadena):

    palabras = cadena.split()
    diccionario = {}

    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in diccionario:
            diccionario[palabra]+= 1
        else:
            diccionario[palabra] = 1
   
    return diccionario

# Solicitar al usuario que ingrese una cadena de caracters

cadena = input("Ingresar cadenas de caracteres:")

# Obtener el diccionario
resultado = contar_palabras(cadena)

for palabra, cant_veces in resultado.items():
    print(f"{palabra} : {cant_veces}")