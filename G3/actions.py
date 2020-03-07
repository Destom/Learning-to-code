def wiper():
    print("\n"*30)

def print_status(character):
    string = f'''name: {character.name}
health: {character.health} / {character.max_health}
attack: {character.attack}
defence:{character.defence}
purse currently holds {character.gold}
{character.inventory}'''
    return string
