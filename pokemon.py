class Pokemon:
    pokekodex = []

    def __init__(self, **kwargs):
        self.name = None
        self.pokemon_type = None
        self.xp = 0

        for key, value in kwargs.items():
            setattr(self, key, value)
        # When everywhere create a pokemon, the kodex will know
        Pokemon.pokekodex.append(self)

    def __str__(self):
        return"Name: {}\nType: {}".format(self.name, self.pokemon_type)

    @staticmethod
    def print_pokekodex():
        print("\nPokekodex:\n"+10*"-")
        for item in Pokemon.pokekodex:
            print(item, '\n')

    @staticmethod
    def get_pokemon_object_name(pokemon_object):
        return pokemon_object.name
