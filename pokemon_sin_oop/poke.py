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


