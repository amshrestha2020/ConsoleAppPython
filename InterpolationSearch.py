'Implement the interpolation search algorithm.'

print("***** Implementation of Interpolation Search Algorithm *****")

def InterpolationSearch(theSeq, key):
    'search element in the list'
    left = 0
    right = (len(theSeq) - 1)
    while left <= right and key >= theSeq[left] and key <= theSeq[right]:
        'estimate the element positioned of list'
        index = left + int(((float(right - left) / (theSeq[right] - theSeq[left])) * (key - theSeq[left])))

        'key value is found'
        if theSeq[index] == key:
            return index

        'discard all elements in the left search'
        if theSeq[index] < key:
            left = index + 1
        else:
            'discard all elements in the right search'
            right = index - 1
    'key does not exist in the list'
    return -1

if __name__ == "__main__":
    theSeq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = int(input("Enter an integer as key :"))
    print("List of items :", theSeq)
    print("Before implementing interpolation search :", (theSeq,key))
    print("***********")
    index = InterpolationSearch(theSeq, key)
    if index != -1:
        print("Element", key, "found at index ", index)
    else:
        print("Element not found in the list.")