def is_palindrome(num):
    #convert all to binary first
    #find number of bits needed
    #subtract 1 to find the highest bit
    #shifts to the left 
    bit = 1 << (num.bit_length() - 1)
    
    # variables used to traverse the whole bits
    right_pointer = num.bit_length() - 1
    left_pointer = 0
    
    while left_pointer < right_pointer:
        # Get the bits left and right positions
        #extracts bit through AND
        left_bit = (num & (1 << left_pointer)) >> left_pointer
        right_bit = (num & (1 << right_pointer)) >> right_pointer
        
        # if bits different then not a palindrome
        if left_bit != right_bit:
            return False
        
        #pointers towards center
        left_pointer += 1
        right_pointer -= 1
        #continues loop until either returns False or finishes scanning
    
    return True

def main():
    print(is_palindrome(220395))  # should print True
    # 220395 is 110101110011101011 in binary (valid palindrome)

    print(is_palindrome(1060))  # should print False
    # 220395 is 10000100100 in binary (not a palindrome)

    print(is_palindrome(75817))  # should print True
    # 220395 is 10010100000101001 in binary (valid palindrome)

    print(is_palindrome(820))  # should print False
    # 220395 is 1100110100 in binary (not a palindrome)

    print(is_palindrome(5557))  # should print True
    # 220395 is 1010110110101 in binary (valid palindrome)


if __name__ == '__main__':
    main()
