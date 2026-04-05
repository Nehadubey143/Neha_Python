'''Tuple :- '''

# => a tuple is a collection of items.
# => it is immutable . 

tupleee = (11,22,33,44)

print(tupleee)

# --------------------------------------- 


tupleee = (11,22,33,44)

print("before :", tupleee)

print(tupleee[2]) ## 33
print(tupleee[-1]) ## 44

print(tupleee[0:3]) # 11,22,33

# --------------------------------------------- 

'''Tuple Methods '''

# count()
# index()

tupleee = (11,22,33,44,22,44,44)

print("before :", tupleee)

print("after: ", tupleee.count(44))

# ------------------------------------------------- 


tupleee = (11,22,33,44,22,44,44)

print("before :", tupleee)

print("after: ", tupleee.index(44)) ## 3