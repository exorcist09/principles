# Dependency Inversion Principle - Corrected using abstraction
from abc import ABC, abstractmethod


# interface
class Persistence(ABC):
    @abstractmethod
    def save_to_db(self):
        pass


# low level modules
class SQLDb(Persistence):
    def __init__(self, data):
        self.data = data

    def save_to_db(self):
        print(f"Saving {self.data} to Sql Db")


class MongoDb(Persistence):
    def __init__(self, data):
        self.data = data

    def save_to_db(self):
        print(f"Saving {self.data} to MongoDb")


# high level module
class Application:
    def __init__(self, persistence):
        self.persistence = persistence

    def save(self):
        self.persistence.save_to_db()


sql = Application(SQLDb({"name": "Adarsh"}))
sql.save()
