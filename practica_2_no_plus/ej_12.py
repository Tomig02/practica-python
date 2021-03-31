
def esBomba(new_string, num_pos, max_pos):
    '''recibre una posicion donde hay una bomba y suma uno a la posicion
    anterior y a la siguiente de la misma fila'''

    new_string += '*'
    if num_pos > 0 and not new_string[num_pos - 1] == '*':
        new_string = sumarPosString(num_pos - 1, new_string)
    if num_pos < max_pos:
        new_string += '1'
    
    return new_string

def sumarPosString(pos, string):
    '''suma uno a la posicion que recibe como parametro en el string que tambien recibe'''

    new_string = string
    num = int(new_string[pos]) + 1

    # convierte el string a lista y suma uno al numero anterior, luego convierte otra vez a string
    string_chars = list(new_string)
    string_chars[pos] = f'{num}'
    new_string = ''.join(string_chars)

    return new_string

def recorrerFila(fila):
    ''' Recorre una fila de el campo de minas, calculando cuantas minas tiene
        alrededor una posicion o si hay una mina, luego devuelve el resultado como un string
    '''

    new_string = ''
    num_pos = 0
    while num_pos < len(fila):
        pos = fila[num_pos]
        if pos == '*':
            new_string = esBomba(new_string, num_pos, len(fila) - 1)
            num_pos += 1
        else:
            new_string += '0'
        num_pos += 1

    return new_string

def sumarFilas(fila_base, fila_suma, max_size):
    ''' toma al primer parametro como fila base y a al segundo como fila sumadora.
        Recorre las filas sumando los valores de la fila sumadora a la fila base, en caso
        de que la posicion de la fila sumadora sea una bomba se toma como un valor de 1.

        - Invocacion: sumarFilas(fila base, fila sumadora, tamaño de los string)
    '''
    pos_num = 0
    fila_base_print = fila_base
    fila_base = list(fila_base)
    
    # recorre la fila y, mientras que la fila base no tenga una bomba,
    # si la fila a sumar tiene una bomba se suma uno a la base, 
    # sino se suma el valor de la posicion de la fila sumadora
    while pos_num < max_size:
        if not fila_base[pos_num] == '*':
            if not fila_suma[pos_num] == '*':
                num = int(fila_base[pos_num]) + int(fila_suma[pos_num])
            else:
                num = int(fila_base[pos_num]) + 1
            fila_base[pos_num] = f'{num}'

        pos_num += 1
    print(fila_base_print, ' + ', fila_suma, ' = ', ''.join(fila_base))

    return ''.join(fila_base)


campo = [
    '--*-*--',
    '*-----*',
    '-*-*-*-',
    '--*--*-',
    '*---*--'
]
campo_num = []
pos_max = len(campo[0])

for pos in range(len(campo)):
    fila_act= recorrerFila(campo[pos])
    campo_num.append(fila_act)

    if pos > 0:
        fila_ant_suma = campo_num[pos - 1]

        new_string_act = sumarFilas(fila_act, fila_ant, pos_max)
        new_string_ant = sumarFilas(fila_ant_suma, fila_act, pos_max)

        campo_num[pos - 1] = new_string_ant
        campo_num[pos] = new_string_act
    
    fila_ant = fila_act

print('')
print('Resultado:')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for pos in range(len(campo)):
    print('         ', campo[pos], '         ', campo_num[pos])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('')



