# Warmup Section

# Question 1

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if (a %2==0) and (b %2==0):
        return min(a,b)
    else:
        return max(a,b)
print("Question 1: ")
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# Question 2

# ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#     word = text.split()
#     return word[0][0] == word[1][0]
def animal_crackers(text):
    word = text.split()

    if word[0][0] == word[1][0]:
        return True
    else:
        return False
print("Question 2: ")
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# The second set of code is what I initially had done. But it is better if I do the first one and not return True or False in the statement.

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if (n1 + n2 == 20) or (n1 == 20 or n2 == 20):
        return True
    else:
        return False
print("Question 3: ")
print(makes_twenty(20,10))
print(makes_twenty(9,3))

# LEVEL 1 QUESTIONS:

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'

# def old_macdonald(name): # Strings are immutatble so I have to split the string into a list.
#     capitalizedString = name.split()
#     print(capitalizedString)
#     # return capitalizedString[0][3].upper() # = name[0:3].upper()
#     return capitalizedString[0:3].capitalize()
#
# print("Question 4: Level 1")
# print(old_macdonald('macdonald'))

# I cannot figure this one out.
# Solution on Stack Overflow
def old_macdonald(name):
    capList = list(name)
    capList[0] = capList[0].upper()
    capList[3] = capList[3].upper()
    return ''.join(capList) # Going to have to get familiar with ''.join(abcdef) as it comes up a lot I see.
print("Question 4: Level 1")
print(old_macdonald('macdonald'))