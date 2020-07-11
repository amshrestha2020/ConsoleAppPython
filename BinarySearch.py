'Implement Binary Search Algorithm.'

print("***** Implementation of Binary Search Algorithm *****")

# def BinarySearch(theSeq, low, high, element):
#     while low <= high:
#         mid = low + (high-low)//2
#         if theSeq[mid] == element:
#             return mid
#         elif theSeq[mid] < element:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
# theSeq = [3, 5, 8, 4, 1, 9, -1, 6, 0, 2, 7]
# element = 1
# low = 0
# high = len(theSeq) - 1
# Check = BinarySearch(theSeq, low, high, element)
# if Check != -1:
#     print("Element is present at index " + str(Check))
# else:
#     print("Not found")

def BinarySearch(theSeq, element):
    first = 0
    last = len(theSeq)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if theSeq[mid] == element:
            index = mid
        else:
            if element<theSeq[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

if __name__ == "__main__":
    theSeq = [10, 20, 30, 40, 50]
    element = 20
    print("List of items :", theSeq)
    print("Enter an element :", element)
    print("No. of element found from the list :",BinarySearch([10, 20, 30, 40, 50], 20))
