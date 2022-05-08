class ItemBase:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} Price: {self.price} Wight: {self.weight}"


class CommonItem(ItemBase):
    pass


class Weapon(ItemBase):
    pass


if __name__ == "__main__":
    sword = Weapon("Sword", 20, 10)
    hammer = Weapon("Hammer", 30, 20)

    bread = CommonItem("Bread", 5, 3)
    milk = CommonItem("Milk", 3, 2)
    cheese = CommonItem("Cheese", 10, 3)

    shopping_list = [bread, sword, hammer, milk, cheese]
    for item in shopping_list:
        print(item)