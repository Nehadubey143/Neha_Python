'''Some important questions :-'''

# my_listt = []

# i have to insert 5 elements in this empty list . 

# => range(5)
# => append()
# => input()


my_listt = []

for i in range(5):
                    element = int(input("enter your element : "))
                    my_listt.append(element)
print(my_listt)

# # --------------------------------------------- 



# create an empty list and insert 10 elements , and if elemnt is 0 then it should be existed at the last.



my_list = []

for i in range(6):
                    element = int(input("enter your element "))

                    if element == 0:
                                        my_list.append(element)
                    else:
                                        my_list.insert(0,element)
print(my_list)





# Function :- 

# => it is a block of code . 
# => it can increase our code reusabaility. 
# => it can save our time . 
# => it can increase code readablity.


def print_all_student_name():
                    print("Gulaam")
                    print("Neha")
                    print("Palak")
                    print("Rohit")

print_all_student_name()
print("second time ")
print_all_student_name()

a = 10 
b = 20 
if a > b:
                    print("a is greater ")
else:
                    print("b is greater")


print_all_student_name()