# what is loop:-it is used to perform any repeated task.

# task: we have to print "NEHA" 10 times.

# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")
# print("NEHA")


# same task we can do with the help of loop.

for i in range(10):
    print("NEHA")


'''TYPES:'''
# 1. For Loop
# 2. While Loop
# 3. do while(not supported in python)

for i in range(0,5):
    print(i)

# i>- loops variable
# satating point => 0
# ending point => 5 , excluded
# final range => 0,1,2,3,4

for i in range(3,9):
    print(i)

# output => 3,4,5,6,7,8
# ---------------------------------------------------------------


for i in range(8):
    print(i)

# satarting point => 0
# ending point => 8 , excluded
# range => 0 to 7
# ---------------------------------------------------------------

for i in range(0,8):
    print(i)

# NOTE: by default stating point will be always 0


for i in range(2,21,2):
    print(i)


# starting point => 2
# ending point => 21 , excluded
# gap => 2 (N - 1) => 2 - 1 = 1 , that's why we have to skip 1 element.

# output => 2,4,6,8,10,12,14,16,18,20   

# 1 task => we have to print table of 39

for i in range(39, 391, 39):
    print(i)


#  2 task>- we have print all the even numbers from 1 to 100

for i in range(2,101,2):
    print(i)
# output => 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100
# --------------------------------------------------------------------


# using for loop by list

my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)
# output => 1,2,3,4,5,6,7,8,9,10

# task ->  we have to print 6 friend name by using for loop and list.

my_friends = ["Neha","Suhani","Palak","Nisha","khushi","Sahana"]

for i in my_friends:
    print(i)