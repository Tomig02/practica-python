import string

# dec variables
string_in = input('Ingresar string para cifrar: ')
caracteres = list(string_in)

# funcion del cifrado cesar
sig_ascii = lambda car, vuelta: chr( (( ord(car) + 1 - 97) % vuelta) + 97 )

# suma 1 al valor ascii de cada caracter, 
# si el valor da mayor a z sigue desde la a
cifrado = ''
vuelta = len(string.ascii_lowercase)
for car in caracteres:
    if car.islower():
        cifrado += sig_ascii(car, vuelta)
    else:
        cifrado += sig_ascii(car.lower(), vuelta).upper()

    
print('String cifrado: ', cifrado)