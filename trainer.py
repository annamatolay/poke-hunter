class Trainer:
    available_pokemon_names = ["Charizard", "Squirtle", "Bulbasaur"]

    def __init__(self, **kwargs):
        self.name = "New Trainer"
        self.age = None
        self.gender = ["female", "male"]
        self.energy = 10
        self.starting_pokemon_object = None
        self.location_object = None
        self.pokemons_objects = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    # I had to... for now the trainer is well-printed
    def __str__(self):
        return "\nYour data\n"+9*"-"+"\nName: {0}\nAge: {1}\nGender: {2}\nEnergy level: {3}\nLocation: {4}".format(
            self.name, self.age, self.gender, self.energy, self.location_object.name)

    def go_to_sleep(self):
        self.energy += 10
        print("\nYour energy level increased!")

    # It's time to use the get_distance_from!
    def go_to_city_object(self, city_object):
        distance = self.location_object.get_distance_from(city_object)
        result = self.energy-(round(distance/10))
        if result > 0:
            self.energy = result
            self.location_object = city_object
            print("You're there now.")
        else:
            print("You don't have enough energy for this trip.. :(")

    def get_pokemon_object_from_location(self):
        if self.location_object.available_pokemon_object is not None:
            self.pokemons_objects.append(self.location_object.available_pokemon_object)
            self.location_object.available_pokemon_object = None
            print("You're succeed!")
        else:
            print("No pokemons here :(")

    def print_pokemons_objects_name(self):
        print("You catch them:")
        for element in self.pokemons_objects:
            print(element.name)

