'Implementation of Linear Search Algorithm.'

print("***** Implementation of Linear Search Algorithm *****")

theSeq = [3, 5, 8, 4, 1, 9, -1, 6, 0, 2, 7]
print("The list of items :", theSeq)
n = int(input("Enter a number to search :"))

def LinearSearch():
    i = flag = 0
    while i < len(theSeq):
        if theSeq[i] == n:
            flag = 1
            break
        i += 1
    if flag == 1:
        print("By using linear search algorithm, item found at position :", i+1)
    else:
        print("The number is available in the list.")

if __name__ == "__main__":
    LinearSearch()


