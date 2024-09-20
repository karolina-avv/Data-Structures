#check if expression has balanced parantheses (stack)

def parentheses(expression):
    #using a dictionary 
    stack = []

    match= {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            #check if opening parentheses are equal
            if not stack:
                return False
            top= stack.pop()
            if top != match[char]:
                return False
            
    return not stack


expression1 = "((()))"
expression2 = "(()"
print(parentheses(expression1))  # Output: True
print(parentheses(expression2))  # Output: False
