# reverse elements in an array

def reverse_elements(arr):
    left= 0
    right= len(arr) -1

    while left<right:
        arr[left], arr[right]=arr[right], arr[left]

        left+=1
        right-=1


my_array = [1, 2, 3, 4, 5]
reverse_elements(my_array)
print(my_array) 
