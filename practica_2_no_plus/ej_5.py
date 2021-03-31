string = input('ingresar un string: ')
palabra = input ('ingresar una palabra')

# inicia variables, limpia arreglo y pasa a minusculas
array_pal = string.lower().replace(',', '').replace('.', '').split()
palabra = palabra.lower()
cant = 0

# busca palabras repetidas y las cuenta
for pal in array_pal:
    if palabra == pal:
        cant += 1

print(cant)