# string methods :- 


# Task: Explore at least 10 string methods 

# upper()   => it converts all characters in uppercase.
# lower()  => it converts all characters in lowercase.
# capitalize() => it converts the first character of first word in uppercase .
# title()  => it converts the first character of each word in a sentence.
# strip()  => it removes the extra space.
# replace() => it replaces a word or character with another word or character.
# split() => it Split a string into a list.
# find() => find the first occurence position of a character or word.
# startswith() => checks if the string starts with a specific word.
# endswith()

# # index()  => find the position of a substring or any character . 

# count() => it counts how many times a character or a word appears in my string . 


my_string = "Python is a Programming Language"
print("before any operation:", my_string)

print("after any operation:", my_string.upper())

# ------------------------------------------------------------ 


my_string = "Python is a Programming Language"
print("before any operation:", my_string)

print("after any operation:", my_string.lower())

# -------------------------------- 


my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.capitalize())

# ---------------------------------------------------------------- 

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.title())


# ------------------------------------------------------


my_string = "             python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.strip())

# --------------------------------------------------------- 


my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.replace("python", "Java"))


# ----------------------------------------------------- 


my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.split())

# ----------------------------------------------------------- 

my_string = "Programming"
print("before any operation:", my_string)

print("after any operation:", my_string.find("P"))
print("after any operation:", my_string.find("m"))

# ---------------------------------------------------------- 

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.startswith("Programming")) # False 
print("after any operation:", my_string.startswith("python")) # True

# --------------------------------------------------------------- 


my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.endswith("Language")) # False 
print("after any operation:", my_string.endswith("language")) # True

# ---------------------------------------------------- 


my_string = "programming"
print("before any operation:", my_string) 

print("after any operation:", my_string.index("m")) # 6 , similir to find() method

# ---------------------------------------------------- 

my_string = "programming"
print("before any operation:", my_string) 

print("after any operation:", my_string.count("m")) # 2

# ---------------------------------------------------------------- 

# NOte: len() is a property of string , it's not a method

my_string = "programming"
print("before any operation:", my_string) 

print("after any operation:", len(my_string) )