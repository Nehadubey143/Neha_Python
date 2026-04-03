# 1.mutable:- it can be changed entirely as well as specific.
# example - list, set, dict

# 2.immutable:- it can be changed entirely but not  specific..
# example - int, float, string, tuple


# 1. why string is immutable? prove this

my_name = "Neha"
print("before:", my_name)

my_name = "Ankit"
print("after:", my_name)

# -------------------------------------------

# my_name = "Neha"
# print("before:", my_name)   

# my_name[0] = "A"   # TypeError: 'str' object does not support item assignment

# ---------------------------------------------

# 2. why list is mutable? prove this

my_list = [1, 2, 3, 4]
print("before:", my_list)

my_list[0] = "Suhani"
print("after:", my_list)
