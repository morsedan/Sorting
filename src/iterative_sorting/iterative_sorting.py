# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr.insert(i, arr.pop(smallest_index))
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    should_repeat = True
    while should_repeat:
        should_repeat = False
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                should_repeat = True
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

list = [9, 5, 4, 6, 3, 7, 2, 8, 1, 0]
print("Bubble sort:", bubble_sort(list.copy()))
print("Selection sort:", selection_sort(list.copy()))