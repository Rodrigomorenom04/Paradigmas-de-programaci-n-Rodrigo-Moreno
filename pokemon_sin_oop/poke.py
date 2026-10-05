"""
Batalla pokemon sin OOP
"""

def crear_pokemon(nombre: str, tipo: str, hp: int, ad: int) -> dict:
    pokemon = {
        'nombre': nombre.capitalize(),
        'tipo': tipo,
        'hp': hp,
        'ad': ad
    }
    return pokemon


def recibir_dano(pokemon: dict, hp_perdido: int) -> None:
    pokemon['hp'] = pokemon['hp'] - hp_perdido


def obtener_ataque(tipo: str) -> str:
    if tipo == 'electrico':
        ataque = 'Impactrueno'
    elif tipo == 'planta':
        ataque = 'Hoja navaja'
    elif tipo == 'fuego':
        ataque = 'Llamarada'
    else:
        ataque = 'Cañon de agua'

    return ataque


def atacar(atacante: dict, rival: dict) -> None:
    ataque = obtener_ataque(atacante['tipo'])

    recibir_dano(rival, atacante['ad'])

    print(f'\n({atacante["nombre"]}) Ataca con {ataque} | -{atacante["ad"]}')


def mostrar_pokemon(pokemon: dict) -> str:
    info_text = f'\n{pokemon["nombre"]} | HP: {pokemon["hp"]}'
    return info_text



