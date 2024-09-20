def find_missing(lis):
    #sum of elements in list
    a=0

    try:
        l=lis[0]
    except IndexError: #if empty list
        return None
    
    for i in lis:
        if l<i:
            l=i #updates max value of list
        a+=i #calc sum of elements in list
        
    total= l * (l+1)/2
    
    if len(lis)==l: #if equal no missing items
        return None
    else:
        newtotal= total-a
        return int(newtotal)


def main():
    lis = [i for i in range(1, 5) if i != 2]
    print(find_missing(lis))  # should print 2

    lis = [i for i in range(1, 49) if i != 40]
    print(find_missing(lis))  # should print 40

    lis = [4, 1, 3]
    print(find_missing(lis))  # should print 2


if __name__ == '__main__':
    main()
