class Person:
    def __init__(self, name, age, address=None, email=None):
        self.name = name
        self.address = address
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Address: {self.address} Email: {self.email}"

    def __repr__(self):
        return self.name


robert = Person("Robert Vari", 38, "Pécs", "robert@gmail.com")
csaba = Person("Kiss Csaba", 40, "Budapest", "csaba@gmail.com")
kriszta = Person("Kriszta", 35, "Kecskemét", "kriszta@gmail.com")
csilla = Person("Csilla", 32, "Budapest", "csilla@gmail.com")


my_friends = [robert, csaba, kriszta, csilla]
print(my_friends)
print(robert)