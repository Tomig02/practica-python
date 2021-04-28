import PySimpleGUI as sg

def crear():

    button = lambda text, key: sg.Button(text, key = key, size = (40, 3), button_color='#2f2f2f')
    layout = [
        [button('Los cantantes mas populares de spotify', '-OP1-')],
        [button('Los atletas olimpicos con mas medallas', '-OP2-')],
        [button('Cerrar', '-SALIR-')]
    ]

    return sg.Window(
        'ventana', 
        layout = layout,
        disable_close = True,
        margins=(100, 50),
        background_color= '#1f1f1f',
        grab_anywhere = True,
    )