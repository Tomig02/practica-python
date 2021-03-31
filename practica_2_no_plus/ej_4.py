
# cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")

# if len(cadena) > 10:
#     print("Ingresaste más de 10 carcateres")
# cant = 0
# for car in cadena:
#     if car == "@" or car == "!":
#         cant = cant + 1
# if cant >= 1:
#     print("Ingresaste alguno de estos símbolos: @ o !" )
# else:
#     print("Ingreso OK")


# simplificado:

cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !): ")
error = False

if len( cadena ) > 10:
    print( "Ingresaste más de 10 carcateres" )
    error = True

if "@" in cadena or "!" in cadena:
    print( "Ingresaste alguno de estos símbolos: @ o !" )
    error = True

if not error:
    print("Ingreso OK")
