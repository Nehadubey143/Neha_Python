'''three parameter string slicing :'''

# first parameter => starting point 
# second parameter => ending point 
# third parameter => GAP ( N - 1 )

# By default Gap will be 1 . 

# # 0 1 2 3 4 5 6 7 8 9 10
# # P r o g r a m m i n g

my_string = "Programming"

print(my_string[0:5]) # P r o g r

# starting point => 0 
# ending point => 5 ( excluded )
# output => 0 - 4 ,  P r o g r

# -------------------------------------------------------------- 


# # 0 1 2 3 4 5 6 7 8 9 10
# # P r o g r a m m i n g

my_string = "Programming"

print(my_string[0:5]) # P r o g r

# print(my_string[0:5 : 1]) # P r o g r
# print(my_string[0: 9 : 2]) # P o r m i

# starting point => 0 
# ending point => 5 ( excluded )
# Gap = 2 , => 2 - 1 => 1, that's why we have to skip 1 element.
# output => P o r m i

# ----------------------------------------------------- 

# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g

my_string = "Programming"


print(my_string[0: 9 : 3]) # 


# starting point => 0
# ending point => 9 ( excluded ) , P r o g r a m m i

# Gap = 3 , => 3 - 1 = 2 , that's why we have to skip 2 elements.
# output => Pgm
# ----------------------------------------------------------------------


# P    r   o   g   r    a    m   m    i     n   g
# -11 -10 -9  -8  -7   -6   -5   -4  -3    -2  -1

# my_string = "Programming"

# print(my_string[-6])  # a

print(my_string[-11 : -6])  # P    r   o   g   r
print(my_string[-9 : -2])  #  o   g   r    a    m   m    i     
print(my_string[-9 : -2 : 1])  #  o   g   r    a    m   m    i    

# print("here is my output :  ", my_string[-1 : -10])

# starting point => -9 
# ending point => -2 , excluded 

# starting point => -11
# ending point => -6  , excluded 


# ---------------------------------------------------------------------- 

# P    r   o   g   r    a    m   m    i     n   g
# -11 -10 -9  -8  -7   -6   -5   -4  -3    -2  -1

my_string = "Programming"

print("here is my output :  ", my_string[ : : ]) 

# starting  point => 0
# ending point => Last Index
# Gap => 1, => 1 - 1 = 0 , that's why we have to skip 0 elements.

# output => P    r   o   g   r    a    m   m    i     n   g

# -------------------------------------------------------------- 
'''Reverse Slicing'''

# P    r   o   g   r    a    m   m    i     n   g
# -11 -10 -9  -8  -7   -6   -5   -4  -3    -2  -1

my_string = "Programming"

print("here is my output :  ", my_string[ : : -1 ]) 

# NOte: whenever you use NEgative Gap , in that case only , the string flow will be right to left