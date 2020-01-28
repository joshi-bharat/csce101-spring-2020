#----------------------------------------
#	Part 3 : Tip Calculator
#----------------------------------------
# We're at a resturaunt and would like to know how much we need to pay
# Let's pretend that we'll always tip 20% and there's a 7% tax. 
# Write a program that prints the tip, the tax, and the final bill.

# Step 1 : Get some input. Remember that since we need to do math with this
# it needs to be converted into a numerical form. Since the bill could be a 
# decimal like 15.95, we'll convert it to a float. 
input_text = input("Type the cost of your food without a $ sign: ") # EG: 35.99
bill_value = float(input_text) # Convert string to float and save the result


# Step 2 : Manipulate the input. To get the % of a number, move the decimal 
# to the left by 2 places and multiply. 20% -> 0.20, 75% -> 0.75, etc
tip_value = bill_value * 0.20  # Tip is 20% of the bill value
tax_value = bill_value * 0.07  # Tax is 7% of the pre-tip bill
total_payment = bill_value + tip_value + tax_value


# Step 3 : Output using multiple print() statements
print("You need to pay a $" , tip_value, " tip.")
print("You're paying $" ,tax_value , " in taxes.")
print("You are gonna be paying $" , total_payment , " tonight.")
#-----------------------------------------------------------------------------
