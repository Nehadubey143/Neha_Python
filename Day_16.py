# my_list = [11,22,33,44]

# for i in my_list:
#                     print(i)

# -------------------------------------------- 

my_name = "Neha"

for i in my_name:
                    print(i)


# ----------------------------------------------- 


for i in range(2):
                    print(i)


# ------------------------ 

# in python 
for i in range(2):
                    print(i)    

# # in  C language 

# for(int i = 0 ; i < 2 ; i++){
#                     printf(i)  ## 0, 1
# }

'''step 1: initialization
step 2: check condition , if condition will be true , in that case only we enter in the loop , 
step 3: run code 
step 4 : increement OR decreement loop varilbe value'''


# Phase 1 

# step 1: initialization

# i = 0
# step 2 : check condition ( i < 2 )

# 0 < 2 => TRUE 

# step 3: run code => print(i)

# step 4 : i increemented by 1 ,  i ++ => 0++ => i = 1


# Phase 2 :-

# step 1: initialization

# i = 1

# step 2 : check condition ( i < 2 )

# 1 < 2 => TRUE 

# step 3: run code => print(i)

# step 4 : i increemented by 1 ,  i ++ => 1++ => i = 2


# Phase 3 :-



# step 1: initialization

# i = 2

# step 2 : check condition ( i < 2 )

# 2 < 2  => False


'''While loop
syntax :-
initialization
while(condition):
    # code to be executed
    # update the condition
'''

i = 0
while(i < 2):
    print(i)
    i += 1


# in C language 


# int i = 0 ;

# while( i < 5){
#                     printf(i);
#                     i ++ ;
# }
                    

# in python
i = 0 

while( i < 5):
                    print(i)
                    i = i + 1

'''
# step 1: initialization
# step 2 : check condition
# step 3 : perform task
# step 4 : increement or decreement '''

# ----------------------------------------------- 

i = 0 

while( i < 2):
                    print(i)  ## 0,1
                    i = i + 1

# Phase 1 :-

# # step 1: initialization
# i = 0 

# # step 2 : check condition

# i < 2 => 0 < 2 => TRUE 

# # step 3 : perform task

# print(i)

# # step 4 : increement or decreement 

# i++ => 0 ++ => 1 

# Phase 2 :-

# # step 1: initialization
# i = 1

# # step 2 : check condition

# i < 2 => 1 < 2 => TRUE 

# # step 3 : perform task

# print(i)

# # step 4 : increement or decreement 

# i ++ => 1 ++ => 2 

# Phase 3 :- 


# # step 1: initialization
# i = 2


# # step 2 : check condition

# i < 2 => 2 < 2 => FALSE


# 1 task: print 1 to 10 using while loop

i = 1   
while(i <= 10):
    print(i)
    i += 1


# 2 task : print name 5 times using while loop

name = "Neha"
i = 0
while(i < 5):
    print(name)
    i += 1

# 3 task : print 1 to 10 using while loop

i = 1
while(i <= 10):
    print(i)
    i += 1

# 4 task : print 5 of table using while loop

i = 5
while(i <= 50):
    print(i)
    i += 5



# task 5 : print reverse of a number using while loop

i = 5
while i >= 1:
    print(i)
    i -= 1