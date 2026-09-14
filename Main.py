"""
Ejemplo vanilla: Gemini API con requests
Para probar la capa gratuita antes de decidir si se usa en clase.

A diferencia de PokeAPI, esta API si pide autenticacion. Para conseguir
una API key gratuita (sin tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google normal
3. Click en "Get API key" y copiar la key que genera

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""
from api_key import API_KEY
import requests

# Pega aqui tu API key (la que copiaste de Google AI Studio).


#constantes
VERBOSE = True
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


#print de configuracion de api 
if VERBOSE:
    print(f'\n ====================')
    print(f'Gemini Model: {MODEL}')
    print(f'api key: {API_KEY}')
    print(f'\n ====================')


    #Construir header con API KEY
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}


#--------- Arriba constante | abajo: dinamico o variante 

while True:

    print(f'\n =================== Gemini =====================')
    User_promt = input("En que piensas?: ")

    if User_promt.lower().strip() == "salir":
        print("Saliendo del programa...")
        break


    body = {
     "contents": [
            {
                "parts": [
                    {"text": User_promt}
                ]   
            }
        ]
    }

    respuesta = requests.post(URL, headers=headers, json=body)

    print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("Algo salio mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        respuesta_gemini = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(respuesta_gemini)



    




