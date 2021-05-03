import PySimpleGUI as sg

def crear_op1(data):
    ''' Crea y retorna una ventana con un layout creado a partir de 
        los datos de la opcion 1
    '''

    # contenedor del layout y una funcion que crea un elemento de texto
    layout = []
    texto = lambda text: sg.Text(text, text_color='#000000', background_color='#eaeaea')
    
    # agrega todas las elementos de el dato recibido como un objeto texto
    # al layout 
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
    ''' Crea y retorna una ventana con un layout creado a partir de 
        los datos de la opcion 2
    '''

    # contenedor del layout y una funcion que crea un elemento de texto
    layout = []
    texto = lambda text: sg.Text(text, text_color='#000000', background_color='#eaeaea')
    
    # agrega todas las elementos de el dato recibido como un objeto texto
    # al layout 
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
    ''' Finaliza la creacion de la ventana, agregandole al layout el
        boton de retorno y creando el objeto ventana
    '''

    # agrega el boton de retorno al layout
    layout.append(
        [sg.Button('Volver', key='-VOLVER-', size=(30,3), button_color='#2f2f2f')]
    )

    # crea la ventana utilizando el layout y desactiva su boton de cierre
    return sg.Window(
        'datos', 
        layout = layout,
        disable_close = True,
        margins=(100, 50),
        background_color= '#1f1f1f',
        element_justification='center'
    )