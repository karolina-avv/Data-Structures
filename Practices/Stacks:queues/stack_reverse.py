def string_reverse(n):
    #use a stack to reverse a string
    stack= []
    for char in n:
        stack.append(char)

    reverse= ''

    while stack:
        reverse += stack.pop()

    return reverse


input_string = "hello"
result = string_reverse(input_string)
print(result)  # Output: "olleh"
    
