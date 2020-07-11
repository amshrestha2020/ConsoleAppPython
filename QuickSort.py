'Implementation of Quick Sort Algorithm'

print("*****  Implementation of Quick Sort Algorithm  *****")

'function to swap values at two indices in the list'
def swap(theSeq, i, j):
    temp = theSeq[i]
    theSeq[i] = theSeq[j]
    theSeq[j] = temp

def partitionSeq( theSeq, first, last):
    'Saving a copy of the pivot value.'
    pivot = theSeq[last]

    'elements less or more than pivot will be pushed to the left or right side of pIndex(pivot Index)'
    'if the elements are of equal then can go either way.'
    pIndex = first

    for i in range(first, last):
        if theSeq[i] <= pivot:
            swap(theSeq, i , pIndex)
            pIndex = pIndex + 1

    'swapping the pIndex with pivot'
    swap( theSeq, last, pIndex)

    return pIndex

def QuickSort(theSeq, first, last):
    if first >= last:
        return

    pivot = partitionSeq(theSeq, first, last)

    QuickSort(theSeq, first, pivot - 1)

    QuickSort(theSeq, pivot + 1, last)

if __name__ == "__main__":
    theSeq = [3, 5, 8, 4, 1, 9, -1, 6, 0, 2, 7]
    print("Before implementing quick sort :", theSeq)
    QuickSort(theSeq, 0, len(theSeq) - 1)
    print("After implementing quick sort :",theSeq)
