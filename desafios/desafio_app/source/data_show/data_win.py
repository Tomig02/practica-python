import PySimpleGUI as sg

def crear_op1(data):
    layout = []
    texto = lambda text: sg.Text(text, text_color='#000000', background_color='#eaeaea')
    
    for i, item in enumerate(data, 1):
        
        layout.append(
            [   texto( ('Posicion:' + f'{i}').center(12) ), 
                texto( ('Nombre: ' + item['name']).center(50) ),
                texto( ('Seguidores: ' + item['followers']).center(25) ),
                texto( ('Populatidad: ' + item['popularity'] + '%').center(20) )
            ]
        )
    return final_creacion(layout)

def crear_op2(data):
    layout = []
    texto = lambda text: sg.Text(text, text_color='#000000', background_color='#eaeaea')
    
    for i, item in enumerate(data, 1):
        layout.append(
            [   texto( ('Posicion: ' + f'{i}').center(12) ), 
                texto( ('Nombre: ' + item['nombre']).center(50) ),
                texto( ('Genero: ' + item['genero']).center(25) ),
                texto( ('Nacionalidad: ' + item['pais']).center(25) ),
                texto( ('Medallas: ' + str(item['medallas'])).center(20) )
            ]
        )
    return final_creacion(layout)
    
def final_creacion(layout):
    layout.append(
        [sg.Button('Volver', key='-VOLVER-', size=(30,3), button_color='#2f2f2f')]
    )

    return sg.Window(
        'datos', 
        layout = layout,
        disable_close = True,
        margins=(100, 50),
        background_color= '#1f1f1f',
        element_justification='center'
    )