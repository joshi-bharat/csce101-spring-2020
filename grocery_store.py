# This is example of sample grocery store for Lab 02

#just try to behave good with customers. You can atleast say hi.
print("hey !! How are you today? ")

#You can enter the number of apples and oranges being ordered
# Remember to take input from keyboard we use input()
noofapples = input("How many apples you want to order ? ")
nooforanges = input("How many oranges you want to order ? ")

# Whatever we get from keyboard is stored as integer.
# Since we entered numbers and need to do calculation on those numbers,
# we convert them to numbers using float()

noofapples = float(noofapples)
nooforanges = float(nooforanges)


rate_for_apple = 0.47
rate_for_orange = 0.52

# Now we have go no. of apples and price of one apples
# To get the total cost we have to multiply no. of apples by rate of apples
# Need to do the same for bananas
# Total is the sum of total for apples and babanas
total = noofapples * rate_for_apple + nooforanges * rate_for_orange

# since the tax is 7%, we can get the tax by multiplying by 0.07
tax = 0.07 * total

#The grand total is total + tax
grand_total = total + tax

# Finally, display the total you got
# You can display a string and number side by side separating them by commas
print("The total is : ", grand_total)

