from Handler import Handler
from Database import Database

class PostHandler(Handler):
    def handler(self, pokemon_identifier):
        if self.pokemon_in_db(pokemon_identifier) is not True:
            return 'Post pokemon successful.'
        else:
            return 'This pokemon already in database.'
            
    def pokemon_in_db(self, pokemon_identifier):
        db = Database().connect_to_db('0.0.0.0', 'rick', '12345678').db
        if pokemon_identifier not in db:
            self.create_new_pokemon_to_database()
            return False

    def create_new_pokemon_to_database(self):
        pass
