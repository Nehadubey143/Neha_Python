# # list methods 

# 1. append() => it is used to add a single element at the end of list.

listt = [11,22,33,44,55]
print("before", listt)
listt.append(66)
print("after ", listt)
# ------------------------------------------

# 2. extend() => it is used to add multiple element at the end of list .

listt = [11,22,33,44,55]
print("before", listt)
listt.extend([66,99])
print("after ", listt)

# ---------------------------------------- 

# 3. insert() => it is used to adds an element at a specific index.

listt = [11,22,33,44,55]
print("before", listt)
listt.insert(2,88)
print("after ", listt)

# ------------------------------------------

# 4. remove() => it is used to remove any specific element .

listt = [11,22,33,44,55]
print("before", listt)
listt.remove(33)
print("after ", listt)

# ------------------------------------------


# 5. pop() => by default it removes the last index value otherwise it removes spcified index value.

listt = [11,22,33,44,55]
print("before", listt)
listt.pop()
print("after ", listt)
# ------------------------------------ 

listt = [11,22,33,44,55]
print("before", listt)
listt.pop(0)
print("after ", listt)

# ------------------------------------------- 

# 6. clear() => it removes entire elements from any list. 

listt = [11,22,33,44,55]
print("before", listt)
listt.clear()
print("after ", listt)

# -------------------------------------- 


# 7. index() => it finds the index of specifed element. 


listt = [11,22,33,44,55]
print("before", listt)
print("after ", listt.index(33))

# ----------------------------------------- 


# 8. count() => it counts how many times a value appears in a list. 
listt = [11,22,33,44,55,33,33]
print("before", listt)
print("after ", listt.count(33))



# --------------------------------------------- 


# sort() => by default it arranges elemnts in asceding order . 


listt = [111,22,33,44,55,33,33]
print("before", listt)
listt.sort()
print("after ", listt)

# ------------------------------------ 

# listt.sort(reverse=True)  ## for descending order

listt = [111,22,33,44,55,33,33]
print("before", listt)
listt.sort(reverse=True)
print("after ", listt)

# -------------------------------------- 

listt = [111,22,33,44,55,33,33]
print("before", listt)
listt.reverse()
print("after ", listt)


# ------------------------------------ 

listt = [111,22,33,44,55,33,33]
print("before", listt)
my_list = listt.copy()
print("after ", listt)
print("my list : ", my_list)