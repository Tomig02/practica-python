import PySimpleGUI as sg
from source.data_show import data_win

def start(data, key):

    ventana = None
    if key == '-OP1-':
        ventana = data_win.crear_op1(data)
    else:
        ventana = data_win.crear_op2(data)
        
    mostrar(ventana)

def mostrar(ventana):
    while True:
        key, _value = ventana.read()

        if key == '-VOLVER-':
            ventana.close()
            break