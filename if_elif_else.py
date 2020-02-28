# In this class we will discuss the if..elif...else using waking up example we discussed in class.

# The syntax of if else is as follows

'''

elif is short form of else if.

if condition1:
    do something here if condition 1 is satisfied

elif condition2:
    do something here if condition 2 is satisfied.
    Remember that condition 2 reaches only if condition 1 is not satisfied.

elif condition3:

.....

else:
    do something if none of the conditions are satisfies

Notes: After each condition there is colon(:)
you put something inside if by indenting with tab

'''


# We extend upon the previous example.
# Now you have one more choice.
# You can come to college  by foot , use Uber or drive to college.
# Since we have more than 2 conditions, we use if..elif..else.
#
# So, you want write a program which decides to go by foot or take Uber or drive to school by taking the wake up time as input.
# The criteria is if you go by foot if you wake up before 8:30  otherwise
# if you wake up between 8:30 and 9, you have enough time to drive to school and find parking space.
# We will use 8.5 for 8:30 as it is easier to compare as number.

#Get wakeup time from keyboard
wake_up_time = input("When did you woke up? ")

#convert into float() so that you can compare
wake_up_time = float(wake_up_time)

#If you woke before 8.5, go by foot
if wake_up_time <= 8.5:
    print(" You got up in time. Lets go strolling to college")

#if you woke up before 9, drive by car.
# you might be wondering 8 is also less than 9, so why does not it print drive by car
# that's because you check less than 9, only after previous condition is not satisfied
# which actually means you woke up after 8.5 and before 9

elif wake_up_time <= 9:
    print(" You have enough time to park your car. take the car")
else:

    #if both of the previous
    print(" Lazy person you forgot the alarm. Take the uber \
          and spend your savings")

