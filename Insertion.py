#credits: Kacper Lodzinski 2020
#Title Insertion Sort Python Implementation

def array_input():
    userInputElems = input("please provide the numbers you like to be sorted(keep space between elements): ")
    array = userInputElems.split()
    return array

def mergeSort(array):
    return 0

def selectionSort(array):
    return 0

def quickSort(array):
    return 0

def insertionSort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while array[currentPosition - 1] > currentValue and currentPosition > 0:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue
        print(array)
    print(array)



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
    
    