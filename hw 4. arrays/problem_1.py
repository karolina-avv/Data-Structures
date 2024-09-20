import ctypes


class UserDefinedDynamicArray:
    def __init__(self, capacity, I=None):
        self._n = 0
        self._capacity = capacity
        self._A = self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self, newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, i):
        if isinstance(i, slice):
            A = UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)):
                A.append(self._A[j])
            return A
        if i < 0:
            i = self._n + i
        return self._A[i]

    def __delitem__(self, i):
        if isinstance(i, slice):
            for j in reversed(range(*i.indices(self._n))):
                del self[j]
        else:
            if i < 0:
                i = self._n + i
            for j in range(i, self._n - 1):
                self._A[j] = self._A[j + 1]
            self[-1] = None  # Calls __setitem__
            self._n -= 1

    def __str__(self):
        return "[" \
            + "".join(str(i) + "," for i in self[:-1]) \
            + (str(self[-1]) if not self.is_empty() else "") \
            + "]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        for i in range(self._n):
            yield self._A[i]

    def __setitem__(self, i, x):
        if i < 0:
            i += self._n
        self._A[i] = x


class RingBuffer(UserDefinedDynamicArray):
    def __init__(self, capacity=5):
        super().__init__(capacity)

    def is_full(self):
        return len(self) == self._capacity

    def is_empty(self):
        return len(self) == 0
        
    def enqueue(self, item):
        if len(self)== self._capacity:
            self.dequeue()
        self.append(item)

    def dequeue(self):
        if len(self)!=0:
            i= self[0]
            del self[0]
            return i

    def resize(self):
        if len(self)> self._capacity //2:
            self._resize(2*self._capacity)
        else:
            self._resize(self._capacity //2)


def main():
    buffer = RingBuffer(5)
    for i in range(1, 6):
        buffer.enqueue(i)
    print(buffer.is_full())  # Output: True
    buffer.enqueue(6)
    print(buffer.is_full())  # Output: True
    print(buffer.dequeue())  # Output: 2
    print(buffer.dequeue())  # Output: 3
    print(buffer.is_empty())  # Output: False
    print(buffer.dequeue())  # Output: 4
    print(buffer.dequeue())  # Output: 5
    print(buffer.is_empty())  # Output: True

    buffer = RingBuffer(5)
    for i in range(1, 6):
        buffer.enqueue(i)
    buffer.resize()
    for i in range(6, 11):
        buffer.enqueue(i)
    print(buffer.is_full())  # Output: True
    for _ in range(10):
        buffer.dequeue()
    buffer.resize()
    #print(buffer._capacity)  # Output: 5


if __name__ == '__main__':
    main()
