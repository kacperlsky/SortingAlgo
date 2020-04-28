#credits: Kacper Lodzinski 2020
#Title Insertion Sort Python Implementation

def array_input():
    userInputElems = input("please provide the numbers you like to be sorted(keep space between elements): ")
    array = userInputElems.split()
    return array

def mergeSort(array):
    return 0

def selectionSort(array):
    newArray= list()

    for i in range(len(array)):
        minval = min(array)
        newArray.append(minval)
        indexMinVal = array.index(minval)
        del(array[indexMinVal])
        print("{} stage".format(i+1), newArray + array)
    print(newArray)
    
    """
    basic version using only one array instead of rewritting 2 arrays

    for i in range(len(array)): 
        minId = i 
        for j in range(i+1, len(array)): 
            if array[minId] > array[j]: 
                minId = j 
                 
        array[i], array[minId] = array[minId], array[i] 
    """

def quickSort(array):
    return 0

def insertionSort(array):
    for i in range(1, len(array)):
        Val = array[i]
        Pos = i

        while array[Pos - 1] > Val and Pos > 0:
            array[Pos] = array[Pos -1]
            Pos = Pos - 1
        array[Pos] = Val
        print("{} Stage".format(i), array)
    print("Final array", array)



if __name__ == "__main__":
    sortingChoice = int(input("Hey, please enter the number and choose one of the following sorting algorithms: \n 1-Insertion Sort\n 2-Merge Sort\n 3-Quick Sort\n 4-Selection Sort\n Your Choice: "))
    if sortingChoice == 1:
        array = array_input()
        insertionSort(array)
    elif sortingChoice == 2:
        array = array_input()
        mergeSort(array)
    elif sortingChoice == 3:
        array = array_input()
        quickSort(array)
    elif sortingChoice == 4:
        array = array_input()
        selectionSort(array)
    else:    
        print("ïnvalid choice")
    
    