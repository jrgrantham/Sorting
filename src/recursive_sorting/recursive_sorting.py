# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    # determine the next largest number to add.
    # add it to the merged array and stop it being reused
    # repeat until all numbers are used in both arrays

    # for i in range(elements):
    #     if (len(arrA) > 0 and len(arrB) > 0):
    #         merged_arr[i] = arrA.pop(0) if arrA(0) < arrB(0) else arrB.pop(0)
    #     elif len(arrA) == 0:
    #         merged_arr[i] = arrB.pop(0)
    #     else:
    #         merged_arr[i] = arrB.pop(0)
    # return merged_arr

    if len(arrA) == 0 or len(arrB) == 0:
        return arrA or arrB

    # x, y = 0, 0

    x = 0
    y = 0
    
    # print(x)
    # print(y)

    while len(merged_arr) < elements:
        if arrA[x] <= arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
        else:
            merged_arr.append(arrB[y])
            y += 1
        if x == len(arrA) or y == len(arrB):
            merged_arr.extend(arrA[x:] or arrB[y:])

    return merged_arr

# print(merge([1],[2]))
# print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 8, 9, 10]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

print(merge_sort([2, 3, 4, 5, 6, 2, 3, 4]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
