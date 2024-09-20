#remove duplicates in an array

def remove_duplicates(arr):
    count= []

    for element in arr:
        if element not in count:
            count.append(element)

    return count

my_array = [1, 2, 2, 3, 4, 4, 5, 5]
result = remove_duplicates(my_array)
print(result)  # Output: [1, 2, 3, 4, 5]
