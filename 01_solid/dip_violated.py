# Dependency Inversion Principle - Violated


# Low-level modules

class SQLDB:
    def save(self, data):
        print(f"Saving {data} to SQL")


class MongoDB:
    def save(self, data):
        print(f"Saving {data} to MongoDB")


# High-level module
class Application:
    def __init__(self):
        self.sql = SQLDB() # has a relationship as we create object of that class in this class
        self.mongo = MongoDB()

    def save_to_sql(self, data):
        self.sql.save(data)

    def save_to_mongo(self, data):
        self.mongo.save(data)


app = Application()
app.save_to_sql({"name": "Adarsh"})
app.save_to_mongo({"name": "Adarsh"})
