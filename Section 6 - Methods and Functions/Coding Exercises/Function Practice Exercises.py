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

# The way the guide did it: (Although my answer is better here.)
def lesser_of_two_evens(a,b):
    if (a % 2 == 0) and (b % 2 == 0):
        #BOTH NUMBERS ARE EVEN
        if a < b:
            result = a
        else:
            result = b
    else:
        # ONE OR BOTH NUMBERS ARE ODD.
        if a > b:
            result = a
        else:
            result = b

    return result

# Can clean it up even more:
def lesser_of_two_evens(a,b):
    if (a % 2 == 0) and (b % 2 == 0):
        #BOTH NUMBERS ARE EVEN
        result = min(a,b)
    else:
        # ONE OR BOTH NUMBERS ARE ODD.
        result = max(a,b)
    return result


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

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
#
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
#
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    reverseSentence = text.split()
    #print(reverseSentence)
    reverseSentence.reverse()
    #print(reverseSentence)
    return " ".join(reverseSentence)

print("Question 5: ")
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
#
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if (n <= 110 and n >= 90) or (n <=210 and n >= 190):
        return True
    else:
        return False
print("Question 6: ")
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


# EVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(num):
    for i in range(len(num)-1): # I forgot to include the -1 at first. This is very important so it doesn't get index out of bounds error.
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False

print("Part 2: Question 7: ")
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = ""
    for i in text:
        result += i*3
    return result

print("Part 2, Question 2: ")
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c): #I didn't read "given 3 numbers at first, woops"
    total = a + b + c
    if total <= 21:
        return total
    elif 11 in (a,b,c) and total - 10 <= 21: # I was getting an error here by doing total(a,b,c).
        return total - 10
    else:
        return "BUST"


    # if numbers.sum() <= 21:
    #     return numbers
    # elif numbers.sum() > 21 and numbers == 11:
    #     numbers -= 10
    # elif numbers.sum() > 21:
    #     return "BUST"


    # sum = 0
    # # for i in numbers:
    #     # if (numbers [i] < 1) or (numbers [i] > 11):
    #         # print("Invalid numbers: Try again.")
    # if sum <= 21:
    #     return sum
    # elif sum >= 21 and numbers == 11:
    #     return sum - 10
    # elif sum > 21:
    #     return "Bust"

print("Part 2: Question 3")
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


# SUMMER OF ('69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). '
#            'Return 0 for no numbers.)
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(numbers):
    sumOfnumbers = 0
    ignoreSection = False

    for num in numbers:
        if ignoreSection:
            if num == 9:
                ignoreSection = False
        else:
            if num == 6:
                ignoreSection = True
            else:
                sumOfnumbers +=num
    return sumOfnumbers
    # # for num in numbers:
    #     if numbers[i] != 6:
    #         sumOfnumbers += numbers[i]
    #     elif numbers[i] == 6:
    #
    # return sumOfnumbers

print("Part 2: Final Question ")
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# This question was very tricky. You want to check to make sure the ignore section is done first before summing the numbers.

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,7,2,0,4,5,0) --> False

def spy_game(numList):
    position = 0
    for num in numList:
        if position == 0 and num == 0:
            position += 1
        elif position == 1 and num == 0:
            position += 1
        elif position == 2 and num == 7:
            return True

    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))

# Also a very tricky one. Created a for loop to track the position within the list and match it with 007.

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
#
# By convention, 0 and 1 are not prime.

# def count_primes(primeNum):

# print(count_primes(100))

# Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
#
# out:   *
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):
    if letter == 'a':
        print("  * " + "\n * *" + "\n*****" + "\n*   *" + "\n*   *")
    elif letter == 'b':
        print("*****" + "\n*  **" + "\n***" + "\n*  **" + "\n*****")

print("Bonus question!")
print(print_big('a'))
print(print_big('b'))