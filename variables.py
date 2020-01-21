#-----------------------------------------------------------------------------
# Section A: Variables
#-----------------------------------------------------------------------------
#----------------------------------------
#	Part 1 : Storing values in variables
#----------------------------------------
# For now, think of variables as named containers for values. 
# They allow us to store values and use them at a later point in the program.
x = 5          # <-- Store the number 5 in a variable named x
print(x)       # Outut: 5
name = "Billy" # <-- Store the text "Billy" in a variable named name
var = 23       # <-- Store the number 23 in a variable named var
asdfgjgk = 2   # <-- Store the number 2 in a variable named asdfgjgk
foo = "bar"    # <-- Store the text "bar" in a variable named foo

# We can change the value of variable as we keep writing the program.
# Variables store values. For example, variables are like glass which can hold
# water, beer, juice or any other liquid or even solid in some cases.
# Let's try one example of glass as variable.

glass = "beer" # <-- There is beer in glass now
print(glass)   # <-- Should print beer as the thing we stored in glass is beer.
# Now, mom and dad are home. We can't drink beer.
glass = "juice" # <-- Put juice in glass
print(glass)   # <--Should print juice as there is juice in glass.
glass = "water" # <-- Too much juice yeah. Let's have some water
print(glass)    # <--Should print water

# Moral: the value of variable is not fixed and can contain anything.

#----------------------------------------
#	Part 2 : Using variables
#----------------------------------------
# We know how to store values. Now let's get around to using them.
# We can use a handy function called print() to help with that. print() just
# takes whatever you put in the parentheses and prints it to the screen.
print("Hi") # <-- Prints "Hi" to the screen
print()     # <-- Nothing is in the parentheses. Prints an empty line
print(x)    # <-- Prints whatever we stored in x (it's 5) to the screen
print(name) # <-- Prints "Billy" to the screen. It was stored back on line 36

# We can also change the contents of the variable by assigning a new value.
name = "Not Billy" # <-- Store the text "Not Billy" in the variable name
print(name)        # <-- Prints "Not Billy" to the screen
name = "Fred"      # <-- Store the text "Fred" in the variable name
print(name)        # <-- Prints "Fred" to the screen
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Section C : Manipulating Variables and Data
#-----------------------------------------------------------------------------
#----------------------------------------
#	Part 1 : Data types
#----------------------------------------

# There are three types of basic data types in python
# 1. String - used as str()
# 2. Integer - used as int()
# 3. Float - used as float()

# One really important thing to know is that Python doesn't treat all values
# the same. Notice how things in quotes behave differently to variables?
print(x)      # <-- Prints whatever we stored in x (it's 5) to the screen
print("x")    # <-- Literally prints the letter x to the screen
print(name)   # <-- Prints the contents of name (it's "Fred") to the screen
print("name") # <-- Literally prints "name" to the screen.

# That's because things in quotes are text. 
# The official name for these pieces of text is Strings. For those of you 
# who were having trouble when writing print("x"), this is why. 
# If you put it in quotes, it's a string.
# Strings get highlighted in a different color than variables as well.
"I am a string"   # <-- Truth. This is a string
I_am_a_variable   # <-- Truth. This is a variable
aNormalVariable   # <-- Truth. This is a variable
"aNormalVariable" # <-- Lies. This is a string. Notice the quotes and color
"I_am_a_variable" # <-- Yet more lies. Again, notice the quotes and color
x                 # <-- A trustworthy variable
"x"               # <-- Don't let strings fool you. They are always text

# A string is a specific type of data. Now let's talk about numbers.
# Numbers that are always whole numbers are called Integers.
# If it's a real number (whole numbers + decimals), then it's Floating Point.
# You will usually see floating point numbers called "Floats".
5       # This is an integer
3.14    # This is a float
4096    # This is an integer
2.71828 # This is a float



# For the things we'll do in lab right now, you only have to worry 
# about the difference between Strings and Numbers. Later you will need to
# know the difference between Floats and Integers, so don't ignore
# the information above.

