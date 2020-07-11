'Implementation of Merge Sort Algorithm'

print("*****  Implementation of Merge Sort Algorithm  *****")

def MergeSort(theSeq):
    print("Splitting ",theSeq)
    if len(theSeq)>1:
        mid = len(theSeq)//2
        lefthalf =theSeq[:mid]
        righthalf =theSeq[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                theSeq[k]=lefthalf[i]
                i=i+1
            else:
                theSeq[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            theSeq[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            theSeq[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ", theSeq)



if __name__ == "__main__":
    theSeq = [3, 5, 8, 4, 1, 9]
    print("Before implementing merge sort")
    print(theSeq)
    print("After implementing merge sort")
    MergeSort(theSeq)
    print(theSeq)

