
# recibe el input sin caracteres especiales o mayusculas
palabra = input("ingrese un heterograma: ")
palabra = ''.join([car for car in palabra if car.isalpha]).lower()

# recorre la palabra asegurandose de que no se repitan las letras
es_eterograma = True
caracteres = set({})
for car in palabra:
    if car in caracteres:
        es_eterograma = False
        break
    else:
        caracteres.add(car)

if(es_eterograma):
    print("Es un heterograma!")
else:
    print("No es un heterograma :c")