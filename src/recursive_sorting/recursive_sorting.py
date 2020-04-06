# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(merged_arr)):
        if arrA == []:
            merged_arr[i] = arrB.pop(0)
        elif arrB == []:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrA.pop(0) if arrA[0] <= arrB[0] else arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    arr1 = merge_sort(arr[:len(arr) // 2])
    arr2 = merge_sort(arr[len(arr) // 2:])
    return merge(arr1, arr2)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr

from random import randint

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[randint(0, len(arr) - 1)]
    lhs = [item for item in arr if item < pivot]
    rhs = [item for item in arr if item > pivot]
    return quicksort(lhs) + [pivot] + quicksort(rhs)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

numbers = [1, 2, 9, 3, 8, 4, 7, 5, 6]
numbers_2 = [5, 6, 4, 7, 3, 8, 2, 9, 1, 0]
# print(quicksort(numbers.copy()))
# print(quicksort(numbers_2.copy()))
print(merge_sort(numbers.copy()))
print(merge_sort(numbers_2.copy()))
# print(merge([5], [3]))
# print(merge([1, 3, 5, 8, 9], [0, 4, 6, 7]))