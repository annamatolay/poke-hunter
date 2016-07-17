"""
Created by Pál Matolay
Really thanks for opportunity to Benedek Vörös!
"""
from pokemon import Pokemon
from city import City
from trainer import Trainer
"""
Create some pokemons, and cities with alone or pokemons.
"""
ch = Pokemon(name='Charizard', pokemon_type='Fire')
sq = Pokemon(name='Squirtle', pokemon_type='Water')
bs = Pokemon(name='Bulbasaur', pokemon_type='Grass')

bp = City(name='Budapest', available_pokemon_object=Pokemon(name='Caterpie', pokemon_type='Bug'))
kv = City(name='Kaposvár', available_pokemon_object=Pokemon(name='Weedle', pokemon_type='Poison'))
hb = City(name='Hajdúszoboszló', available_pokemon_object=Pokemon(name='Pikachu', pokemon_type='Electric'))
db = City(name='Debrecen', available_pokemon_object=None)

# Create the basic of player
player = Trainer(location_object=bp)

"""
"Tutorial" or prologue in the game. The player create your own character.
"""

print("Welcome to the PokeHunter 1.0")
print("All instructions or available choices will be in [] .. Follow them! ;)")
input("[Any button to skip]")
player.name = input("I greet you, stranger! My name is professor Oak. What's yours?\n")
age = input("And.. How old are you?\n")
while True:
    try:
        player.age = int(age)
        break
    except ValueError:
        age = input("Please, give me a number!\n")
gender = input("I see not well, so please, tell me! What is your gender?\n[female/male]\n")
while gender not in player.gender:
    gender = input("Please, select an available!\n")
player.gender = gender
starting_pokemon_object = input("I can offer one pokemon from below.\n[Charizard/Squirtle/Bulbasaur]\n")
while starting_pokemon_object not in Trainer.available_pokemon_names:
    starting_pokemon_object = input("Please, select an available!\n")
if starting_pokemon_object == 'Charizard':
    player.starting_pokemon_object = ch
elif starting_pokemon_object == 'Squirtle':
    player.starting_pokemon_object = sq
elif starting_pokemon_object == 'Bulbasaur':
    player.starting_pokemon_object = bs
player.pokemons_objects.append(player.starting_pokemon_object)
print(player)
input("[Any button to skip]")
print("\nNow the whole world is yours!\nAll pokemons waitng for you!\nGotta catch'em all! ;)")
input("[Any button to skip]\n")

"""
Finally, the game, and the menu loop.
"""

"""
OPTIONS:
- quit 0
- print(player) 1
- Pokemon.print_pokekodex() 2
- player.print_pokemons_objects_name() 3
- City.print_available_cities_with_pokemon() 4
- player.go_to_sleep() 5
- player.go_to_city_object(city_object) 6
- player.get_pokemon_object_from_location() 7
"""

OPTIONS = []
# [0, 1, 2, 3, 4, 5, 6, 7]
OPTIONS.extend(range(0, 8))
print("[You can choose an option, if press an available number, then hit the enter.]")
while True:
    print("""
    0: Quit the game
    1: "Look in the mirror"
    2: Lovely Pokekodex
    3: Precious collection
    4: "Where is the next Pokemon?"
    5: I go to sleep!
    6: Let's trip!
    7: Catch the pokemon!!!
        """)
    while True:
        try:
            opt = int(input())
            break
        except ValueError:
            print("I asked a number, not else...")
    if opt == 0:
        print("Thanks for playing!\nI hope you enjoyd :)")
        break
    elif opt == 1:
        print(player)
    elif opt == 2:
        Pokemon.print_pokekodex()
    elif opt == 3:
        player.print_pokemons_objects_name()
    elif opt == 4:
        City.print_available_cities_with_pokemon()
    elif opt == 5:
        player.go_to_sleep()
    elif opt == 6:
        available_cities = [bp, kv, hb, db]
        counter = 0
        print("Available cities:\n"+"-"*18)
        for element in City.available_pokemon_object:
            print("-", element.name, "[{}]".format(counter))
            counter += 1
        while True:
            try:
                answer = int(input("Give me the target city number!\n"))
                break
            except ValueError:
                print("I asked a number, not else...")
        if 0 <= answer < 4:
            city_object = available_cities[answer]
            player.go_to_city_object(city_object)
        else:
            print("Wrong number!")
    elif opt == 7:
        player.get_pokemon_object_from_location()
    else:
        print("Invalid number!")

