from Handler import Handler
from Database import Database

class PutHandler(Handler):
    def handler(self, pokemon_identifier):
        if self.pokemon_in_db(pokemon_identifier):
            return 'Put pokemon successful.'
        else:
            return 'This pokemon not in database.'
            
    def self.pokemon_in_db(self, pokemon_identifier):
        db = Database().connect_to_db('0.0.0.0', 'rick', '12345678').db
        if pokemon_identifier in db:
            self.put_new_pokemon_info_to_database()
            return True

    def put_new_pokemon_info_to_database(self):
        pass
