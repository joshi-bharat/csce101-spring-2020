#	Part 1 : Add Two Numbers
#----------------------------------------
# Let's say we're asked to write a program that asks the user for two numbers,
# then add those numbers and display the sum.

# Step 1 can be solved using the input() function. Since not all items can be
# treated as text, you may need to use int(), float(), etc in order to 
# get them into a number. You can just wrap the thing you want to 
# convert in parentheses as shown below.
text_input1 = input("Enter the first number: ")
number_version1 = float(text_input1)
text_input2 = input("Enter the second number: ")
number_version2 = float(text_input2)

# Step 2 can be accomplished using operators such as +, -, *, / to modify the
# data. In this case we can just multiply it.
addition = number_version1 + number_version2


# Step 3 is usually done using the print() function.
# You can print two different types using commas ,
print("The sum of these two numbers is : " , addition) 
