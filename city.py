import urllib.request
import unicodedata
import string


class City:
    available_pokemon_object = []
    available_cities = ['Budapest', 'Kaposvár', 'Hajdúszoboszló', 'Debrecen']

    def __init__(self, **kwargs):
        self.name = None
        self.available_pokemon_object = None

        for key, value in kwargs.items():
            setattr(self, key, value)
        City.available_pokemon_object.append(self)

    # Sometimes this is very slow....
    def get_distance_from(self, city_object):
        # Doesn't matter the accents or other special character
        def remove_accents(data):
            return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters)
        # Get the cities
        from_city = remove_accents(self.name)
        where_city = remove_accents(city_object.name)
        # Great API from google
        web_obj = urllib.request.urlopen(
            "http://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}".format(
                from_city, where_city))
        results_string = str(web_obj.read())
        web_obj.close()
        # Normalize the giant string, and get the valuable data
        results_string = results_string.split(" ")
        result_km = results_string[87:88]
        result_km = result_km[0].split("\"")
        return round(int(result_km[1]))

    @staticmethod
    def print_available_cities_with_pokemon():
        try:
            for element in City.available_pokemon_object:
                print("There is a {} in {}".format(element.available_pokemon_object.name, element.name))
        except AttributeError:
            pass
