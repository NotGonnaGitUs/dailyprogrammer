import itertools

letters = itertools.permutations(input("Enter the text to print permutations of"))
for each in letters:
    print ("".join(each))
