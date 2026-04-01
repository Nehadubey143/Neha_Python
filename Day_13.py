
# list string indexing and String slicing 

# my_list = [11, 22, 33, 44, 45]
#            -5  -4  -3  -2  -1

my_list = [11,22,33,44,45]
print(my_list[-1]) ## 45

print(my_list[ : ]) ## 11,22,33,44,45

print(my_list[1: ])  ## 22,33,44,45

print(my_list[ -3 : ]) ## 33,44,45

print(my_list[-1 : ]) ## 45

print(my_list[0: : 2]) ## 11 33 45

print(my_list[: : -1 ]) ## 45 44 33 22 11