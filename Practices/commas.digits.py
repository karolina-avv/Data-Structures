#function adding commas to correctly represent digits

def commas(num):
    if num<1000:
        return str(num)
    else:
        rest= num // 1000
        three_digits= num % 1000
        return commas(rest)+ ',' + str(three_digits)

    
def main():
    num = int(input("Enter a number: "))  # You can replace this with any integer you want
    result = commas(num)
    print(f"Number with commas: {result}")

if __name__ == "__main__":
    main()
