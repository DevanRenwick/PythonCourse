# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
# Assume that the incoming string only contains letters, and don('t worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so '
#                                                                'long as letters alternate throughout the string.)
def myfunc(x):
    random_string = []
    for index in range(len(x)):
        if index % 2 == 0:
            random_string.append(x[index].upper())
        else:
            random_string.append(x[index].lower())
    return "".join(random_string)

# This was challenging for what I know of Python so far. Got a lot of help from the course form.