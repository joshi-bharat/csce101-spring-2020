# In this class we will discuss the if..else using waking up example we discussed in class.

# The syntax of if else is as follows

'''

if condition1:
    do something here if condition 1 is satisfied

else:
    do something if none of the conditions are satisfies

Notes: After each condition there is colon(:)
you put something inside if by indenting with tab

'''


# We have a situation here. You are let's say 20 mins walking distance from college.
# You can come to college  by foot or use Uber.
# You have a class at 9:30
# So, you want write a program which decides to go by foot or take Uber by taking the wake up time as input.
# The criteria is if you go by foot if you wake up before 8:30  otherwise by Uber.
# We will use 8.5 for 8:30 as it is easier to compare as number.

# You are just setting up a reminder here. Hope you succeed.
print('You have a class at 9:30 am. Wake up early ')

# Enter the wake up time. Better wake up on time.
wakeuptime = input("Enter when you woke up").strip()

# You have to convert to float
wakeuptime = float(wakeuptime)

if wakeuptime < 8.5:
    # If you wake up before 8.5 then you got to college strolling. The condition wakeuptime < 8.5 will
    # only be true if you wake up before 8.5
    print("Nice job buddy. you can now go strolling to college !!")

else:
    # Else is activated only if the previous conditions are not satisfied.
    # which means you could not wake up before 8:30 and had to take uber.
    print("Get off bed you lazy person. Take a uber and empty your savings !!")