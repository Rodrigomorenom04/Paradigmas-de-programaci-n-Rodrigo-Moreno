"""
Batalla pokemon sin OOP
"""
from random import sample
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


def mostrar_seleccionados(poke_1: dict, poke_2: dict) -> None:
    print('\n ------ POKEMON SELECCIONADOS ------')

    waiting()
    print(f'\nPokemon 1: {poke_1["nombre"]} (HP: {poke_1["hp"]} | AD: {poke_1["ad"]})')
    print(f'Pokemon 2: {poke_2["nombre"]} (HP: {poke_2["hp"]} | AD: {poke_2["ad"]})')



def perdio(pokemon: dict) -> bool:
    if pokemon['hp'] <= 0:
        return True
    else:
        return False


def turno(atacante: dict, rival: dict) -> bool:
    waiting()
    atacar(atacante, rival)

    if perdio(rival):
        print(f'\nGAME OVER: {atacante["nombre"]} venció a {rival["nombre"]}')
        return True

    return False


def mostrar_hps(poke_1: dict, poke_2: dict) -> None:
    waiting()
    print('\nHPs restantes')
    print(f'{poke_1["nombre"]}: {poke_1["hp"]}')
    print(f'{poke_2["nombre"]}: {poke_2["hp"]}') 


def batalla(poke_1: dict, poke_2: dict) -> None:
    while True:

        # Turno poke_1
        if turno(poke_1, poke_2):
            break

        # Turno poke_2
        if turno(poke_2, poke_1):
            break

        mostrar_hps(poke_1, poke_2)



def main() -> None:
    inventario = crear_inventario()

    seleccionados = seleccionar_pokemon(inventario)
    poke_1 = seleccionados[0]
    poke_2 = seleccionados[1]

    mostrar_seleccionados(poke_1, poke_2)
    batalla(poke_1, poke_2)


main()
