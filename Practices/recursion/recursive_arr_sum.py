#find sum of elements in an integer array using recursion

def recursive_sum(arr, idx):
    #if length is bigger than 0 then exceeds limit
    if idx >= len(arr):
        return 0
    else:
        return arr[idx] + recursive_sum(arr, idx+1)


my_array = [1, 2, 3, 4, 5]
result = recursive_sum(my_array, 0)
print("Sum of elements in the array:", result)
