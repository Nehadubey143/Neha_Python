# dictionary :- 

# => it is a collection of data , which is stored in key value pair. 
# => it is mutable . 

my_dictionary = {
                    "name" : "Rohan",
                    "roll" : 111,
                    "course" : "Python"
}

# Left side => Keys 
# right side => Value 



my_dictionary = {
                    "name" : "Rohan",
                    "roll" : 111,
                    "course" : "Python"
}

print(my_dictionary.get("name"))  ## ROhan
print(my_dictionary.keys())  ## 
print(my_dictionary.values())  ## 
print(my_dictionary.items())  ## 

print(my_dictionary.update({"age":23}))  ## 
print(my_dictionary)
# ---------------------------------------------------- 

my_dictionary = {
                    "name" : "Rohan",
                    "roll" : 111,
                    "course" : "Python"
}

print("before", my_dictionary)
# my_dictionary.pop() ## TypeError: pop expected at least 1 argument, 
my_dictionary.pop("roll")  

print("after", my_dictionary)


# ------------------------------------


my_dictionary = {
                    "name" : "Rohan",
                    "roll" : 111,
                    "course" : "Python"
}

print("before", my_dictionary)

my_dictionary.clear()  

print("after", my_dictionary)