# tuples, sets, frozen sets, complex

# Python is a dynamically typed language, so you do not have to declare data types beforehand, unlike C# for example:
#
#   C#
#   int myAge = 39;
#   string myName = "Mr Bancroft"
#
#   Python
#   my_age = 32
#   my_name = "Mr Bancroft"
#
# Languages like C# are known as statically typed languages. There are advantages and disadvantages to Python's approach
# the primary advantage is that the speed of writing code is increased and the primary disadvantage is that subtle bugs
# can easily be introduced into your code when variables are not statically declared#.
# You can emulate statically typed languages in Python now by typing:


def add_numbers(a: int, b: int) -> int:
    return a + b

# This function uses what is known as type hinting, however, is purely for the IDE or end user's benefit, not the
# Python's. Also, be aware that this approach will not work in any version of Python before 3.5. Python will interpret
# this code exactly the same as the following code:


def add_numbers(a, b):
    return a + b

# (By the way, if my formatting looks odd to you try Googling "PEP8") so which is better? Well that depends, example a
# is much less ambiguous than example b, you know the function wants two integers and returns an integer. Example a is
# 17 characters shorter though and over 500 lines of code, that can be a lot of typing. Ultimately it is up to you, the
# coder, to decide which approach is best suited to your project.
# The first function will not provide you with the same protections that a statically typed language will though. You
# can still create errors which will only surface at run time, for example:
#
#   def add_numbers(a: int, b: int) -> int:
#       return a + b
#
#
#   add_numbers(10, "twelve")
#
# will throw an exception when you try to run it because you cannot add an integer and a string in Python. If you are
# using an IDE that supports type hinting, it will warn you before you try to run the code but it will not stop you.

# Python's built-in types

# ********** INTEGERS **********

meaning_of_life = 42

# ********** FLOATING POINT NUMBERS **********

pi = 3.1415926535

# ********** COMPLEX NUMBERS **********

pi_life = meaning_of_life ** pi

# ********** CASTING between types **********

int(pi) == 3
float(meaning_of_life) == 42.0

# ********** STRINGS (unicode in Python 3) **********

my_text = "Hello, world!"
my_quote = 'I always say "there are no silly questions"'
my_wall_of_text = """"I love to write
lines and
lines and
lines and
line of text."""

# you can use single or double quotes but they must match. Triple quotes maintain the formatting of the text and are
# often used in the description of function behaviour by programmers in the code.
# as far as Python is concerned 'hello' == "hello" == """hello"""
# strings have a lot of functions associated with them for manipulating and formatting them, see me lesson on strings to
# learn more

# ********** BOOLEAN (note the capitals) ***********

is_right = True
is_wrong = False

# Converted to integer, a bool is 0 or 1 for False or True

# ********** NONE **********

planets_colonised = None

# None can be handy if you want to create a variable but you do not want to create a variable but you do not want to
# assign it a value immediately. It is also handy in logic statements for example

if planets_colonised:
    print("We are now spacefarers")
else:
    print("We are still Earth bound")

# This will print "We are still Earth bound" as planets_colonised is None which equates to False.

# ********** OPERATORS **********
# A ! symbol is used to denote "not" in checks, so == means "is equal" and != means "is not equal"
# You can also use "and" and "or" keywords in if statements:

if planets_colonised != True and meaning_of_life == 42.0:
    print("We are Earth bound and the meaning of life is still 42.")
else:
    print("Don't ask me, I don't know any more.")
if pi == 3 or pi == 3.1415926535:
    print("Phew Pi is still the same.")
else:
    print("Panic, Pi has changed we are all doomed!!")

# You can also use one line if statements (known as "ternary statements")

a = 1
b = 2
print("bigger") if a > b else print("smaller")

# This will print "smaller" as a is < b

# ********** LISTS **********
# You can think of lists like one dimensional arrays.
# An empty list:

my_list = []

# A list with some contents:

my_list_colours = ["Hazel", "Yellow", "Orange", "Purple", "Blue", "Green", "Red", "Maroon", "Black", "White", "Turquoise",
                   "Magenta", "Cyan", "Plum", "Apricot", "Scarlet", "Beige", "Pink", "Grey"]

# To access a particular colour in the list you refer to its index. Indexes are automatically assigned and begin at 0 so
# Red = 0, Yellow = 1, Orange = 2 and so on. To get Blue you could use code like:

chosen_colour = my_list_colours[4]
print(chosen_colour)

# List index can also work in "reverse" so to get the last entry you can use -1, like so:

chosen_colour = my_list_colours[-1]
print(chosen_colour)

# This returns "Grey"
# Lists have many functions and qualities, a great deal of which can be learnt in the appropriate lesson.

# ********** LOOPS **********
# Loops are an essential part of any program. If you want to find a colour in a list, loops are what you need:

index_count = len(my_list_colours)
found = False
for i in range(0, index_count - 1):
    if my_list_colours[i] == "Red":
        print("Red has been found at index no: " + str(i))
        found = True
if not found:
    print("Red was not found in the list, sorry")

# If we try the same code with a colour not in the list

index_count = len(my_list_colours)
found = False
for i in range(0, index_count - 1):
    if my_list_colours[i] == "Mango":
        print("Mango has been found at index no: " + str(i))
        found = True
if not found:
    print("Mango was not found in the list, sorry")

# Have a think about this, why do you suppose that the loop runs until the length of the list - 1, not the length of the
# list? The answer is further down, see if you are right. (clue, List indexes are zero bound, or start at zero)
# we can also use a loop to print the contents of a List:

index_count = len(my_list_colours)
for i in range(0, index_count - 1):
    print(str(my_list_colours[i]))

# This will print out every item in the list. If you are still wondering why we use the list length - 1, try taking the
# -1 out of the code and see what happens. Which error message do you get? Did it help you to see the reason? If not
# take 2 minutes just to have a think.
# You could of course just type
# print(my_list_colours[0])
# print(my_list_colours[1])
# print(my_list_colours[2])
# print(my_list_colours[3])
# print....
# This, however, becomes very tedious very quickly (that is why we let the computers do the work), can lead to major
# errors (are you sure you know the last index? What happens if someone else on the project adds another colour?) and
# breaks a principle rule of programming known as the DRY / WET principle. In programming we like to be DRY and not WET
# so "Don't Repeat Yourself" rather than "Writing Everything Twice". A huge advantage in using computers is they do this
# kind of operation standing on their heads, with one hand tied behind the back whilst eating a toffee. It is easy for
# them. If you are going to need to do something lots of times, put it in a function and instead of writing the logic
# over and over, just call the function as and when you need it. This also makes changing the code easier as you only
# have to alter the function in one place not many - again reducing the potential for errors.

# the for loop will run a certain number of times so is useful when you know how many times you need to run. What if you
# do not know though? Then you can use a while loop. A while loop will keep running "while" you need it to:

import random
random_start = random.randint(0, 100)
print("Need to get we start with a random number between 1 and 100 to start with:")
while random_start < 101:
    print(str(random_start))
    random_start += 1
    print("plus one = " + str(random_start))
print("We are finished")

# We could of course use a for loop here but it would need extra logic and therefore code. We would have to find how
# many times we need to run first (take the random number from 101) and then count from 1 to the calculated number
# adding one each time. And what if the number keeps changing as a result of something else going on? Well now you see
# the need for a while loop.
# Remember
# for loop == used when you know for certain how many time you are going to iterate through something
# "Do this X times"
# while loop == used when you are uncertain how many times you need to iterate or the number of iteration is variable
# "Do this until Y"
# Loops are explained in more detail in the appropriate lesson. Familiarise yourself with loops they are some of the
# most important building blocks in programming.
