import random
import math

print("Hello, Sir!")
print("In this program you are able to create animals")
print("For creating animals you have to chose the class and input weight")
print("Here are available 4 classes for mammals:")
print("Cow, goat, sheep, pig")
print("And 3 classes for birds:")
print("Duck, chicken, goose")
print("And a secret class, platypus!")
print("Every animal has some limbs")
print("Every animal can sound with the function \"roar\"")
print("Some animals can make some goods with the function \"good\"")
print("You can transform your animal to meat")
print("Amount of meat depends on weight of the animal")
print("But there is some chance that the animal will run off")
print("Like in the movie \"Chicken Run\"")
print("Use the function \"description()\" to know more about the animal")
print("Good Duck!\n")


class Animal:
    sound = None

    def roar(self):
        print(self.sound)

    product = 0

    def good(self):
        if self.product != 0:
            print("You got {}".format(self.product))
        else:
            print("Just meat.")

    hard_product = 0

    def __init__(self, massa):
        self.mass = massa
        self.flesh = round(math.sqrt(self.mass), 2)

    def chicken_run(self):
        if random.randint(1, 10) == 10:
            print("They run off, Sir!")
        else:
            print("You got {} kg of {}".format(self.flesh, self.hard_product))

    def meat(self):
        self.chicken_run()


class Mammal(Animal):
    leg = 4
    tail = 1


class Bird(Animal):
    wing = 2
    beak = 1
    leg = 2
    tail = 1


class Cow(Mammal):
    sound = "Moo!"
    product = "milk"
    hard_product = "beef"


class Goat(Mammal):
    sound = "Bleat!"
    hard_product = "goat's meat"


class Sheep(Mammal):
    sound = "Bleat!"
    product = "fleece"
    hard_product = "mutton"


class Pig(Mammal):
    sound = "Oink!"
    hard_product = "bacon"


class Duck(Bird):
    sound = "Quack!"
    hard_product = "duck's meat"


class Chicken(Bird):
    sound = "Puk-Puk!"
    hard_product = "chicken"


class Goose(Bird):
    sound = "Quack!"
    hard_product = "duck's meat"


class Platypus(Mammal, Bird):
    sound = "I'm not a duck!"
    product = "sense of strangeness"
    wing = 0

    def meat(self):
        print("Ara you sure?")
        answer = str(input()).lower()
        if answer == "yes":
            self.hard_product = "human's meat"
            self.flesh = "a lot"
            super(Platypus, self).meat()
        else:
            print("Good choice")


# Примеры
mimi = Cow(720)
perry = Platypus(1.7)
donald = Duck(1.2)
dolly = Sheep(75)


def description(beast):
    print("Let me introduce to you this animal!")
    print("This is {}".format(type(beast).__name__))
    print("It has:")
    print("   {} legs".format(beast.leg))
    print("   {} tail".format(beast.tail))
    if hasattr(beast, 'wing') and beast.wing != 0:
        print("   {} wings".format(beast.wing))
    if hasattr(beast, 'beak'):
        print("   and a beak!")
    print("It weighs {} kgs".format(beast.mass))
    print("Sounds like \'{}\'".format(beast.sound))
    if beast.product != 0:
        print("And makes {}".format(beast.product))
    if beast.hard_product != 0:
        print(
            "You can make {} from it".format(beast.hard_product),
            "\nbut please, don't do this!"
        )
    print("\nWe are happy to meet you!")

# Примеры работы функций над животными
# mimi.good()
# dolly.roar()
# donald.meat()
# description(perry)
