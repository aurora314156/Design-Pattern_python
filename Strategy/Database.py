
class Database():
    def __init__(self):
        self.db = 'None'

    @db_connect_info.setter
    def db_connect_info(self, address, username, password):
        self.db = connected_db(address, username, password)

    @property
    def db_connect_info(self):
        return self.db
