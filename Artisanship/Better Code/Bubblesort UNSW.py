'''
This code is written by Z.C
It uses the bubble sort method to sort a list
2/06/2018
'''

def bubbleSort(intList):
    
    #Function required just for this function        
    def swap(x,y):
        return y,x
    
    #If they pass in a list of string integers

    # Set finished to false assuming list isn't sorted
    finished = False

    print(' '.join(intList))
    while (finished == False):
        # Sets finished to True and finishes if there are no more switches
        finished = True

        # Minus one since we are comparing two variables at a time
        # Therefore we will compare (len(intList) - 1) variables
        for listNum in range(len(intList)-1):
            if int(intList[listNum]) > int(intList[listNum+1]):
                intList[listNum],intList[listNum+1] = swap(intList[listNum],intList[listNum+1])
                finished = False
                print(' '.join(intList))

amount = int(input())
userInput = input().split()
assert (len(userInput) == amount)
bubbleSort(userInput)
