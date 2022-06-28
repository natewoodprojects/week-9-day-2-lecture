# Nicely done homie. This clears the screen. 
import os 
os.system("clear")

# This is a comment. But it's awesome

# Data Types:
# Strings
# Numbers: Floats amd Integers
# Lists (Arrays)
# Tuples (arrays with rounded brackets that you cannot change)
# Dictionaries (Objects. )
# Escape character \

# first_name = "Nate"
# address = "97 \'Joy Street\'"


# print (first_name, address)

# first_name = "Walter"
# print (first_name, address)

# my_string = "My name is Nate Wood"

# print(my_string[5])

# print (round((2/3), 4))
# my_name = "TakoKing"
# first_names = ["Jen", "Nate", "Jess", my_name]

# first_names[0] = "Alison"

# del first_names[0]

# first_names.append("Alison")

# print(first_names[len(first_names) - 1])

# last_names = ("Wood", "Zumdahl", "Money")
# last_names_2 = ("Wellinghoff",)
# last_names_3 = last_names + last_names_2
# print (last_names_3[0:3])

heroes = {
    "Deku": "All for One",
    "Todoroki": "Fire and Ice",
    "Ida": "Speed"
}

# heroes.update({"Nova": "Human Rocket",})

# print(heroes)

# print ("Ten" == "Ten")

# num = 20
# if (num > 10 and 50 < 100):
#     print("Yup")
# elif (num < 10):
#     print("Nope")
# elif (num == 10):
#     print("Same")
# else: 
#     print("Hmmmm")

# counter = 0

# while (counter < 10):
#     print("The Count is: %s" % counter)
#     counter += 1

# name = ["John", "Bob", "Tina"]

# for key, value in heroes.items(): 
#     print(key, value)


# counter = 0
# while (counter <= 100):
#     if (counter % 15 == 0):
#         print ("%s - FizzBuzz" % counter)
#     elif (counter % 5 == 0):
#         print ("%s - Buzz" % counter)
#     elif (counter % 3 == 0):
#         print ("%s - Fizz" % counter)
#     else:
#         print(counter)
#     counter += 1

# def namer(name): 
#     return ("Hello %s" %name)

# my_namer = namer("Nate")

# for letter in my_namer: 
#     print(100000000)


# print(my_namer.upper())

# import namer_module

# print(namer_module.namer("nate"))

# first_name = "Nate"

# print(first_name.upper())

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

# Methods within a class. Kinda like functions within a  object class in JS
    def area (self):
        return self.side_length * self.side_length

    def peremeter (self):
        return self.side_length * 4

my_square = Square(10)

print(my_square.peremeter())

