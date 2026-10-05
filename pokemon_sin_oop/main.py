"""
Batalla pokemon sin OOP
"""
from random import choice, sample
from time import sleep
from poke import crear_pokemon, atacar



def waiting() -> None:
    print('\n...')
    sleep(0.5)


def crear_inventario() -> list:
    pikachu = crear_pokemon('pikachu', 'electrico', 60, 15)
    chikorita = crear_pokemon('chikorita', 'planta', 45, 10)
    charmander = crear_pokemon('charmander', 'fuego', 40, 10)
    froakie = crear_pokemon('froakie', 'agua', 40, 20)

    inventario = [pikachu, chikorita, charmander, froakie]

    return inventario


def seleccionar_pokemon(inventario: list) -> list:
    seleccionados = sample(inventario, 2)
    return seleccionados



