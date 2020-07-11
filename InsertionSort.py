'Implementation of the Insertion Sort Algorithm.'

print("***** Implementation of Insertion Sort Algorithm  *****")

def InsertionSort(theSeq):
    n = len(theSeq)

    for i in range(1, n):
        'saving the value to the position.'
        value = theSeq[i]
        'Finding the position where values fits in the ordered part of the list.'
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            'During search of items, shift the items to the right side of list'
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        'Putting the saved value into the open slot.'
        theSeq[pos] = value

if __name__ == "__main__":
    theSeq = [3, 5, 8, 4, 1, 9, -1, 6, 0, 2, 7]
    print("Before implementing insertion sort algorithm :", theSeq)
    InsertionSort(theSeq)
    print("After implementing insertion sort algorithm :", theSeq)
