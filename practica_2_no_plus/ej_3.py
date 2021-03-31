texto = """Ayer vi a los caminantes: a los indiferentes, los miedosos, los valientes, los cansados, los enamorados, y los desahuciados.

Ví como sus pasos se convertían en fino polvo al contacto con el inmediato y fugaz presente. Descubrí que a la mayoría el pasado no le servía de nada.

Aún no terminaba de observarlos y el futuro ya se apropiaba de aquel presente, ahora convertido en pasado, mostrándole a cada cual las consecuencias de sus actos.

Continué contemplando el futuro,  hasta el instante en el que la muerte decidió cambiar el camino de los indiferentes, los miedosos, los valientes, los cansados, los enamorados, y los desahuciados."""


letra = input("ingrese una letra: ")

# limpia al texto y lo divide en una lista de palabras 
nuevo_texto = texto.replace(',','').replace('.','').replace(':','')
lista_pal = nuevo_texto.split()

# recorre la lista y imprime las palabras con la letra inicial sin repetir
palabras = []
for palabra in lista_pal:
    if not palabra in palabras and letra == palabra[0] :
        palabras.append(palabra)
        print(palabra)
    