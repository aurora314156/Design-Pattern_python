from Handler import Handler
from Database import Database

class GetHandler(Handler):
    def handler(self, pokemon_identifier):
        if self.pokemon_in_db(pokemon_identifier):
            return 'Your pokemon info.'
        else:
            return 'This pokemon not in database.'
            
    def pokemon_in_db(self, pokemon_identifier):
        db = Database().connect_to_db('0.0.0.0', 'rick', '12345678').db
        if pokemon_identifier in db:
            self.get_pokemon_from_database()
            return True

    def get_pokemon_from_database(self):
        pass
