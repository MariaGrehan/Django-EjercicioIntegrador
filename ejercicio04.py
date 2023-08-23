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

frecuencia = 0
for palabra, cant_veces in resultado.items():
    print(f"{palabra} : {cant_veces}")
    if cant_veces > frecuencia:
        frecuencia = cant_veces
        palabra_res = palabra
        
tupla = (palabra_res, frecuencia)
print("La palabra mas repetida es ", tupla[0], "que se repitio ", tupla[1], "veces")

    
