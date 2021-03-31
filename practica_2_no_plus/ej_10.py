



valores = { ('a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'): 1,
    ('d', 'g'): 2,
    ('b', 'c', 'm', 'p'): 3,
    ('f', 'h', 'v', 'w', 'y'): 4,
    ('k'): 5,
    ('j', 'x'): 8,
    ('q', 'z'): 10,
}

palabra = input('Ingrese una palabra: ')
puntaje = 0
for letra in palabra:
    for valor in valores:
        if letra in valor:
            puntaje += valores[valor]

print('tu puntaje es: ', puntaje)