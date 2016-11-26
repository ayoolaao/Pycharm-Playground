class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

kola = Parent("Abimbola", "Brown")
print(kola.eye_color)

ayo = Child("Kidd", "Blue", 7)
print(ayo.last_name)
print(ayo.number_of_toys)