# if , else
# => In If and else Statement there is two Condition only

a = int(input("Enter your age: "))

if (a < 18):
    print("You are Not An adult")
else:
    print("You are 18+")



# if ,elif ,else
# => In If , elif and else Statement there is Three and more Then Three Condition Can Be Apply


a = int(input("Enter your Number: "))
b = int(input("Enter another number: "))


if (a > b):
    print("a is bigger than b",a)
elif(b > a):
    print("b is bigger than a",b)
else:
    print("Both Values are equal")

a = int(input("Enter Student Marks:"))

print("Student Grade")

if(a > 90 ):
    print("Grade A+")
elif(80 < a < 89):
    print(" grade A")
elif(70 < a < 79):
    print(" grade B+")
elif(60 < a < 69):
    print(" grade B")
else:
    print("Grade F")

# Nested if

# => In Nested Loop There Is Condition inside the Condition

a = int(input("Enter Your age"))

if ( a > 17):
     print("You are An adult and you are capable for voting")
     b = input("Entre your state: ")
     if(b .title()== "Delhi"):
        print("You are capable for vote")
     else:
         print("You are not from the Delhi")
else:
    print("You are not capable for vote")