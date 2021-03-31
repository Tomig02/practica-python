frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
# limpia y divide al array en palabras
array_pal = frase.lower().replace(',','').replace('.','').split()

# guarda las palabras repetidas en un arreglo
pal_rep = []
for pal in array_pal:
    if not pal in pal_rep:
        pal_rep.append(pal)    

print(pal_rep)

