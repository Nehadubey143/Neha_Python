# COnditional stmt => it is used to make decision in your code. 

# if 
# if - else 
# if- elif


Marks = int(input("enter your marks: "))

if Marks > 70 :
                    print("first Division")

if Marks > 60 and Marks < 70 :
                    print("Second Division")





# -----------------------------------------------------------------------

'''example :-'''

# 1. example :-  create a program to check whether the given number is even or odd.

number = int(input("enter your number "))
if number % 2 == 0:
                    print("Even number")
else:
                    print("Odd number")

# -------------------------------------------------------------

# 2. example :-  create a program to check whether the given number is positive or negative.

number = int(input("enter your number "))
if number > 0:
                    print("Positive number")
else:
                    print("Negative number")

# -------------------------------------------------------------

# 3. example :-  create a program to check whether the given number is divisible by 5 or not.

number = int(input("enter your number "))
if number % 5 == 0:
                    print("Divisible by 5")
else:
                    print("Not Divisible by 5")



# -------------------------------------------------------------

# 4. example :-  create a program to check whether the given number is divisible by 3 and 5 or not.



number = int(input("enter your number "))
if number % 3 == 0 and number % 5 == 0:
                    print("Divisible by 3 and 5")
else:
                    print("Not Divisible by 3 and 5")




# statment  