'Implementation of Bubble Sort Algorithm'

print("*****  Implementation of Bubble Sort Algorithm  *****")
'function to swap values at two indices in the list'
def swap(theSeq, i, j):
    temp = theSeq[i]
    theSeq[i] = theSeq[j]
    theSeq[j] = temp

'function to perform bubble sort on list'
def BubbleSort(theSeq):
    n = len(theSeq)
    'perform n-1 bubble operations on the sequence'
    for k in range(n-1):
        'switching the largest item to the end'
        for i in range(n-1-k):
            if theSeq[i] > theSeq[i+1]:
                'swap the i and i+1 items'
                swap(theSeq, i, i+1)


if __name__ == "__main__":
    theSeq = [3, 5, 8, 4, 1, 9, -1, 6, 0, 2, 7]
    print("Before implementing bubble sort algorithm :", theSeq)
    BubbleSort(theSeq)
    print("After implementing bubble sort algorithm :", theSeq)


