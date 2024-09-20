def string_generator():
    # generator so yield command and no recursion!!
    #total= total perms from the letters set
    total = 1
    
    letters = ['c', 'a', 't', 'd', 'o', 'g']
    n = len(letters)

    #generates permutations using total and n
    for i in range(n):
        if n>0:
            total = n * total
            n-=1

    for i in range(total):
        index = len(letters) - 1
        while index > 0 and not letters[index - 1] < letters[index]:
            index -= 1
    
        letters[index:] = reversed(letters[index:])

        if index > 0:
            j = index
            for j in range(index, len(letters)):
                if letters[index - 1] < letters[j]:
                    letters[index - 1], letters[j] = letters[j], letters[index - 1]
                    break

        yield ''.join(letters)

def main():
    cat_dog = string_generator()
    print(next(cat_dog))  # Output: "catdog" or another combination
    print(next(cat_dog))  # Output: "catdgo" or another combination
    print(next(cat_dog))  # Output: "catodg" or another combination


if __name__ == '__main__':
    main()
