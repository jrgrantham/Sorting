import random

example1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
example2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
example3 = random.sample(range(200), 50)

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    # print(arr)
    return arr

selection_sort(example1)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    repeat = True
    while repeat:
        print(arr)
        count = 0
        for i in range(0, len(arr) - 1 ):
            if arr[i] > arr[i+1]:
                count += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if count == 0:
            repeat = False
    return arr

bubble_sort(example2)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr