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

# This method (known as type hinting), however, is purely for the IDE or end user's benefit, not the Python's. Also, be
# aware that this approach will not work in any version of Python before 3.5. Python will interpret this code exactly
# the same as the following code:


def add_numbers(a, b):
    return a + b

# (By the way, if my formatting looks odd to you try Googling "PEP8") so which is better? Well that depends, example a
# is much less ambiguous than example b, you know the function wants two integers and returns an integer. Example a is
# 17 characters shorter though and over 500 lines of code, that can be a lot of typing. Ultimately it is up to you, the
# coder, to decide which approach is best suited to your project.
# The first method will not provide you with the same protections that a statically typed language will though. You can
# still create errors which will only surface at run time, for example:
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

# integer
meaning_of_life = 42

# floating point numbers
pi = 3.1415926535

# complex numbers
pi_life = meaning_of_life ** pi

# casting between types
int(pi) == 3
float(meaning_of_life) == 42.0

# strings (unicode in Python 3)
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

# Boolean (note the capitals)
is_right = True
is_wrong = False
# Converted to integer, a bool is 0 or 1 for False or True

# None
planets_colonised = None
# None can be handy if you want to create a variable but you do not want to create a variable but you do not want to
# assign it a value immediately. It is also handy in logic statements for example
if planets_colonised:
    print("We are now spacefarers")
else:
    print("We are still Earth bound")
# This will print "We are still Earth bound" as planets_colonised is None which equates to False.

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

# Lists
