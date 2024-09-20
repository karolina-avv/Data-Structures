#function finding if a string has more vowels or consonants
#use recursion

def is_vowel(char):
    #check if char is a vowel
    return char.lower() in 'aeiou'

def counter(s, index=0, vowel=0, consonant= 0):
    #base case
    if index== len(s):
        return vowel> consonant

    #stores value of string as lowercase into char
    char= s[index].lower()

    #check if vowels or consonants then increment accordingly
    if char.isalpha():
        if is_vowel(char):
            vowel+=1
        else:
            consonant +=1
    #recursive call to next index in s
    return counter(s, index+1, vowel, consonant)

def has_more_vowels(s):
    return counter(s)

def main():
    result = has_more_vowels('arthritis')
    if result:
        print("There are more vowels.")
    else:
        print("There are more consonants.")

if __name__ == '__main__':
    main()
