import random
import math

print("Hello, Sir!")
print("In this program you are able to create animals")
print("For creating animals you have to chose the class and input weight")
print("Here are available 4 classes for mammals:")
print("Cow, goat, sheep, pig")
print("And 3 classes for birds:")
print("Duck, chiken, goose")
print("And a secret class, platypus!")
print("Every animal has some limbs")
print("Every animal can sound with the function \"roar\"")
print("Some animals can make some goods with the function \"good\"")
print("You can transform your animal to meat")
print("Amount of meat depends on weight of the animal")
print("But there is some chance that the animal will run off")
print("Like in the movie \"Chiken Run\"")
print("Use the function \"description()\" to know more about the animal")
print("Good Duck!\n")


class animal():

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

    def ChikenRun(self):
        if random.randint(1, 10) == 10:
            print("They run off, Sir!")
        else:
            print("You got {} kg of {}".format(self.flesh, self.hard_product))

    def meat(self):
        self.ChikenRun()


class mammal(animal):
    leg = 4
    tail = 1


class bird(animal):
    wing = 2
    beak = 1
    leg = 2
    tail = 1


class cow(mammal):
    sound = "Moo!"
    product = "milk"
    hard_product = "beef"


class goat(mammal):
    sound = "Bleat!"
    hard_product = "goat's meat"


class sheep(mammal):
    sound = "Bleat!"
    product = "fleece"
    hard_product = "mutton"


class pig(mammal):
    sound = "Oink!"
    hard_product = "bacon"


class duck(bird):
    sound = "Quack!"
    hard_product = "duck's meat"


class chiken(bird):
    sound = "Puk-Puk!"
    hard_product = "chiken"


class goose(bird):
    sound = "Quack!"
    hard_product = "duck's meat"


class platypus(mammal, bird):
    sound = "I'm not a duck!"
    product = "sense of strangeness"
    wing = 0

    def meat(self):
        print("Ara you sure?")
        answer = str(input()).lower()
        if answer == "yes":
            self.hard_product = "human's meat"
            self.flesh = "a lot"
            super(platypus, self).meat()
        else:
            print("Good choice")

# Примеры
mimi = cow(720)
perry = platypus(1.7)
donald = duck(1.2)
dolly = sheep(75)


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
