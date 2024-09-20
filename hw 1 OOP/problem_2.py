class IterableIterator:
    #initialised iterator with init function
    def __init__(self):
        self.current = 0

    #in order to make an object iterable, have to make it return itself
    def __iter__(self):
        return self

    #calculates next value
    def __next__(self):
        #used 20 and adding 1 to ensure that iterator restarts after 20
        self.current = (self.current % 20) + 1
        return self.current

    #iterator length is infinite, just restarts from 20 each time
    def __len__(self):
        return float('inf')

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be positive")
        #find value at given index
        return (index % 20) + 1


def main():
    my_obj = IterableIterator()
    my_it = iter(my_obj)
    print(my_obj[41])  # Output: 2
    print(next(my_it), next(my_it), next(my_it), next(my_it))  # Output: 1 2 3 4


if __name__ == '__main__':
    main()
