from api_key import API_KEY
import requests




VERBOSE = True
TEAM_ID = 81  # FC Barcelona
URL = f"https://api.football-data.org/v4/teams/{TEAM_ID}"

if VERBOSE:
    print(f'\n ====================')
    print(f'Team ID: {TEAM_ID}')
    print(f'\n ====================')

headers = {
    "X-Auth-Token": API_KEY,
}



while True:
    print(f'\n =================== Football Data =====================')
    opcion = input("Presiona ENTER para ver info del equipo, o escribe 'salir': ")

    if opcion.lower().strip() == "salir":
        print("Saliendo del programa...")
        break

    respuesta = requests.get(URL, headers=headers)

    if respuesta.status_code != 200:
        print("Algo salio mal:")
        print(respuesta.text)    
    else:
        datos = respuesta.json()
        print(f"\nEquipo: {datos['name']}")
        print(f"Estadio: {datos['venue']}")
        print(f"Fundado: {datos['founded']}")
        print(f"Entrenador: {datos['coach']['name']}")




