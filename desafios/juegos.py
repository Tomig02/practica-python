import csv, requests


with open("./appstore_games.csv") as juegos:
    archivo = list(csv.DictReader(juegos))

    for row in archivo:
        if 'ES' in row['Languages']:
            print(row['Name'])
    
    maximos = (sorted(archivo, key = lambda archivo: archivo['User Rating Count'], reverse= True)[:10])
    
    for i, item in enumerate(maximos):
        icon_url = item['Icon URL']
        icono = requests.get(icon_url)
        with open(f'./imagenes/{i}.jpg', 'wb') as f:
            f.write(icono.content)
