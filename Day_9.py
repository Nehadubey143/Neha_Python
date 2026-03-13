'''String Indexing :- '''

# Positive indexing:-

my_word = "Programming"

#  0 1 2 3 4 5 6 7 8 9 10
#  P r o g r a m m i n g

print(my_word[7])  # m
print(my_word[0])  # P
print(my_word[10]) # g
print(my_word[3])  # g
print(my_word[4])  # r
print(my_word[5])  # a
print(my_word[6])  # m
print(my_word[8])  # i
print(my_word[9])  # n
print(my_word[1])  # r
print(my_word[2])  # o

# Negative indexing:-


my_word = "Programming"

# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  P  r  o  g  r  a  m  m  i  n  g

print(my_word[-1])   # g
print(my_word[-2])   # n
print(my_word[-3])   # i
print(my_word[-4])   # m
print(my_word[-5])   # a
print(my_word[-6])   # r
print(my_word[-7])   # g
print(my_word[-8])   # m
print(my_word[-9])   # o
print(my_word[-10])  # r
print(my_word[-11])  # P

'''String Slicing :-String Slicing :- Slicing ka matlb hota h striing ke andar se kuch part ko Slice karna and index ke help se'''

# For 2 perameters String slicing:

# First perameters = Stating Point.
# Second perameters = Ending Point.

# Some's rules:-
# 1). by defult(pahle se tay hai) Stating point will be always 0.
# 2). by defult Ending point will be always Excluded.
# 3). by defult Ending point will be last index.

# Posetive Slicing:-

#  0 1 2 3 4 5 6 7 8 9 10
#  P r o g r a m m i n g

my_string = "Programming"  # mujhe is me se "gramm" ko slice karna hai

print(my_string)

print("Slicing:",my_string[3:8]) # gramm

# starting point => 3
# ending point => 8 ( excluded ), i.e ending point = 7
# ---------------------------------------------------------------------------------------

# 0 1 2 3 4 5 6 7 8
# n e h a d u b e y

my_name = "nehadubey" # mujhe iis me se "hadub" ko slice karna hai
print(my_name)
print("Slicing:",my_name[2:7]) # hadub

# stating point => 2
# ending point => 7 (excluded) i.e ending point = 6
# -------------------------------------------------------------------------------------------

my_name = "nehadubey" # mujhe iis me se "neha" ko chor kar slice karna hai

print(my_name)
print("Slicing:",my_name[4: ]) # dubey

# Stating point => 4
# Ending point => Last index
# OPUTPUT = 4 to 8 => dubey
# ---------------------------------------------------------------------------------------
my_name = "nehadubey" # mujhe is me ab "nehadubey" ka slicing karna hai

print(my_name)
print("Slicing:",my_name[:])

# Stating point => 0
# Ending Point => Last Index
# OUTPUT = nehadubey
# -----------------------------------------------------------------------------------------

# Negative Slicing:-

# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  P   r   o  g  r  a  m  m  i  n  g

my_string = "Programming" # mujhe is me se "gramm" ko slice karna hai
print(my_string)
print("Slicing:",my_string[-8 : -3]) # gramm

# starting point => -8
# ending point => -3 (excluded) i.e ending point = -4
# --------------------------------------------------------------------------------------
# -9 -8 -7 -6 -5 -4 -3 -2 -1
#  n  e  h  a  d  u  b  e  y

my_name = "nehadubey" # mujhe iis me se "hadub" ko slice karna hai
print(my_name)
print("Slicing:",my_name[-8 : -3]) # hadub

# stating point => -8
# ending point => -3 (excluded) i.e ending point = -4
# --------------------------------------------------------------------------------------

my_name = "nehadubey" # mujhe iis me se "neha" ko chor kar slice karna hai
print(my_name)
print("Slicing:",my_name[-6 : ]) # dubey

# Stating point => -6
# Ending point => Last index
# OPUTPUT = -6 to -1 => dubey
# --------------------------------------------------------------------------------------
my_name = "nehadubey" # mujhe is me ab "nehadubey" ka slicing karna hai
print(my_name)
print("Slicing:",my_name[:]) # nehadubey

# Stating point => 0
# Ending Point => Last Index
# OUTPUT = nehadubey
# ------------------------------------------------------------------------------------------













