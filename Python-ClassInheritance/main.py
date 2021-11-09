class Animal:

    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Under the water")

    def swim(self):
        print("Swim")

fish = Fish()
fish.breathe()
fish.swim()
print(fish.eyes)