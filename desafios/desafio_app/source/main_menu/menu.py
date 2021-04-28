import PySimpleGUI as sg
from source.main_menu import menu_win, menu_func
from source.data_show import data as show_data

def run():

    ventana = menu_win.crear()
    mostrar(ventana)

def mostrar(ventana):
    
    while True:
        key, _value = ventana.read()

        if key == "-OP1-" or key == "-OP2-":
            data = []

            if key == "-OP1-":
                data = menu_func.artistas_famosos(10)
            else:
                data = menu_func.olimpiadas_oro(10)

            cambiar_ventana(ventana, data, key)

        if key == "-SALIR-":
            ventana.close()
            break
    
def cambiar_ventana(ventana, data, key):
    ventana.hide()
    show_data.start(data, key)
    ventana.un_hide()