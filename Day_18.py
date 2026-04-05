'''set :- '''

# => a set is a collection of items , 
# => it can contain only unique elements.
# => it can not contain any duplicate elements
# => it does not support indexing. 
# => it is unordered. 
# => it is mutable .

my_set = {11,22,33,44,11,22}
print(my_set)
print(my_set[4]) ## error 

# set methods :-

''' add()'''
'''remove()'''  #=> it element is not found , it gives error
''' discard()''' #=> it element is not found , it does not give any error
'''pop()''' #=> it remvos any random element

my_set = {11,22,33}
print("before", my_set)

my_set.add(100)
print("after", my_set)

# ----------------------------------------------- 

my_set = {11,22,33}
print("before", my_set)

my_set.remove(11)
print("after", my_set)

# -------------------------------------- 

my_set = {11,22,33}
print("before", my_set)

my_set.discard(111)
print("after", my_set)

# -------------------------------------------- 

my_set = {11,22,33,123}
print("before", my_set)

my_set.pop()
print("after", my_set)

# ---------------------- 


my_set = {11,22,33,123}
print("before", my_set)

my_set.clear()
print("after", my_set)
# -------------------------------------------- 

# in mathematics 

# A = {11,22,33}
# B = {11,22,44}

# print( A Union B )  => 11,22,33,44 (# similar elements and rest of elements )

# print( A intersection  B) => 11,22  ( only similar elements)

# similar elements and rest of elements 



# ------------------------------------------------- 


A = {11,22,33}
B = {11,22,333}

print("union", A.union(B))
print("intersection", A.intersection(B))