'''
By Zachary Cheng
18-04-2018
This code is for Dmoj. Given a string,
it will output all the permutations of the string.
'''

def permutations(items):
    amountOfItems = len(items)
    if amountOfItems == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

variables = []
userInput = list(input())

for i in permutations(userInput):
    variables.append("".join(i))
   
variables.sort()

for var in variables:
    print(var)
