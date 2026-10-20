# Single Responsibility Principle

class UserService:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def profile(self):
        print(f"User: {self.name} with {self.age} lives in {self.address}")


class ProductService:
    def __init__(self, brand, price:int):
        self.brand = brand
        self.price = price

    def get_product(self):
        return f"Product is of {self.brand} brand and is of {self.price}"

    def add_product(self):
        return f"adding product: {self.brand}, price: {self.price}"


class SaveDB:
    def __init__(self, db_name, connection):
        self.db_name = db_name
        self.connection = connection

    def save_to_db(self):
        self.db_name = "Haleluya DB"
        return f"Saving to {self.db_name} with {self.connection}"


def main():
    user = UserService("Adarsh", 23, "Lucknow")
    print(user.profile())

    product = ProductService("Iphone", 1000)
    print(product.get_product())

    saveDB = SaveDB("sql", "sqlalchemy")
    print(saveDB.save_to_db())


if __name__ == "__main__":
    main()
