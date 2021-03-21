try:
    mensaje = int(input("Ingresa un numero: "))
    if mensaje % 2 == 0:
        print("este numero es par")
    else:
        print("este numero es inpar")
except ValueError:
    print("Esto no es un numero!")