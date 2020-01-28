#----------------------------------------
#	Part 1 : Data types
#----------------------------------------

# There are three types of basic data types in python
# 1. String - used as str()
# 2. Integer - used as int()
# 3. Float - used as float()

# One really important thing to know is that Python doesn't treat all values
# the same. Notice how things in quotes behave differently to variables?
x = 5 
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



#----------------------------------------
#	Part 2 : What are operators?
#----------------------------------------
# Operators are just ways of doing something to one or more values. 
# These values don't even have to be variables.
1 + 1  # Add 1 + 1
5 * 5  # Multiply 5 * 5
10 / x # Divide 10 by whatever is stored in x
10 / 2 # Divide 10 by 2
1 - 1  # Subtract 1 from 1
x - 5  # Get the value stored in x and subtract 5. Doesn't save the value

# WARNING: It is important to remember when dealing with variables that the
# value is not modified unless you assign it. As a rule of thumb, if there 
# isn't an = sign somewhere in the symbol, you're not saving the result.
x = 10    # Store 10 in x for this example
x - 2     # Takes the value 10 and subtracts 2 from it
print(x)  # Prints 10, because we never stored the result
x = x - 2 # Takes the value 10 and subtracts 2 from it. Stores 8 back into x
print(x)  # Prints 8, because we stored the result of x - 2 back into x

# With that out of the way, let's get back to operators...
# You can also have multiple operators on the same line. Be careful to 
# keep your code readable. You can group operations with parentheses to make 
# sure they get calculated first.
x = 1
y = 48
z = 0
result = (x * 2) + (y  / 24) * (z + 6) # These lines are all the same
result = (1 * 2) + (48 / 24) * (0 + 6) # These lines are all the same
result = 2 + 2 * 6                     # These lines are all the same
result = 2 + 12                        # These lines are all the same
result = 14                            # These lines are all the same
# NOTE: Division turns ints into floats if one of the values is a float, so 
# you may see a decimal in your answer after dividing some values. 

# We don't just have to add numbers. We can also add strings together.
word1 = "Hello "
word2 = "World"
print(word1 + word2) # "Hello " + "World" equals "Hello World"

# Remember, adding strings is different than adding numbers. String addition
# just sticks the second value onto the end of the first.
word1 = "1"
word2 = "2"
print(word1 + word2) # Prints "12" NOT 3.



#----------------------------------------
#	Part 3 : Operators are picky
#----------------------------------------
# Remember how in Part 1 we discussed the different types of data?
# That was important since operators (usually) don't work on data of 
# different types. Below are examples of bad code that will cause errors.
result = 5 + "Bananna" # Don't mix Numbers and Strings.
result = 1 + "1"       # Even if the string looks like a number, it isn't

# You can't mix types even if you try to do it through a variable. 
sneakyString = "text"  # Store the text "text" into sneakyString
x = 1 + sneakyString   # Attempting to mix Numbers and Strings. This fails

# The example above causes an error:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# If you see any errors in your code that start with TypeError, you are
# probably mixing types that don't go together. 



#----------------------------------------
#	Part 4 : Converting types
#----------------------------------------
# So now that I've told you not to mix types when adding variables, you may be 
# wondering how to get messages that combine variables and text to the screen.
# Since everything the input() function returns is a string, you may also be
# unsure how to do math based on things the user typed in.

# The answer is type conversions.

# Remember print()? It's something called a Function. You don't need to
# know what a function is right now. Just know that you can use a function
# by writing its name, and can usually modify its behavior by putting 
# information in the parentheses.

# You put "Hi" in the parentheses, it will print "Hi".
print("Hi") 

# "Type some input: " is in the parentheses. It will print that and then
# save the user's input into the variable x.
x = input("Type some input: ") 

# Well, print() and input() aren't the only functions out there. There are
# functions that turn one type of data into another.
x = int("120")   # Turns the string "120" into the Integer 120, stores it in x
x = float("120") # Turns the string "120" into the Float 120.0, stores it in x
x = str(120)     # Turns the Integer 120 into the string "120", stores it in x


# When you are printing different data types, you need to separate them by commas\
# print( string, integer, float)

# So let's say we want to print a message + the contents of a variable with
# a number inside. We want it to say "The value is : 240" when we're done.
number_var = 240
print("The value is : " , number_var)      # Prints - The value is 240

float_num = float(120.9)        #float_num is a Float Variable
int_num = int(10)               #int_num  is integer Variable
string_var = str("Hello")       # string_var is string Variable
print(string_var,  float_num, int_num)  #Prints all of them on same line
                                #Output : Hello 120.9 10


#Below we will look how turn strings into numbers.


# Remember that text is a string. The user's input will be a string
first_number = input("Type a number: ")         # Let's pretend we type 1
second_number = input("Type another number: ")  # Let's pretend we type 1

# Remember that when adding text, we just stick the two pieces together. So
# if we type "1" and "1" for each number, the line below will print "11" 
# instead of 2. In order to do this correctly, we need to convert strings to
# ints
print(first_number + second_number) # This doesn't do the math correctly
#This will print 11 because both the first_number and second_number are strings
# Adding two strings means concatinating them

#By using the int() function, we will now get the right answer
print(int(first_number) + int(second_number)) # These will add correctly
#-----------------------------------------------------------------------------







