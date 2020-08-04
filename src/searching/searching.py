def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    search_arr = arr
    low_index = 0
    high_index = len(arr) - 1
    while len(search_arr) > 0:
        
        if search_arr[(low_index + high_index)//2] == target:
            return (low_index + high_index)//2
        elif search_arr[(low_index + high_index)//2] > target:
            high_index = (low_index + high_index)//2
        else:
            low_index = (low_index + high_index)//2
            
    return -1  # not found
