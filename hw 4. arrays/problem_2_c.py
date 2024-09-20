import ctypes

class UserDefinedDynamicArray:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A=UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __delitem__(self,i):
        if isinstance(i,slice):
            for j in reversed(range(*i.indices(self._n))):
                 del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]    
            self[-1]=None        
            self._n-=1
        if self._n*4<=self._capacity:
          self._resize(self._capacity//2)

    def __str__(self):
        return "[" \
               +"".join( str(i)+", " for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        for i in range(self._n):
          yield self[i]

    def __setitem__(self,i,x):
        if i<0:
            i += self._n
        self._A[i]=x

    def extend(self,I):
        for i in I:
          self.append(i)

    def reverse(self):
        for i in range(self._n//2):
            self[i]= self[self._n-i-1]
            self[self._n-i-1]= self[i]

    def __contains__(self,x):
        for i in range(self._n):
            if self._A[i] == x:
                return True
        return False
        
    def index(self,x):
        for i, item in enumerate(self.data):
            if item == x:
                return i
        return None

    def count(self,x):
        count=0
        for i in self:
          if x==i:
            count+=1
        return count


    def __add__(self,other):
        new=UserDefinedDynamicArray(self)
        new.extend(other)
        return new
          
    def __mul__(self,times):
        new= UserDefinedDynamicArray()
        for i in range(times):
            new.extend(self)
        return new

    __rmul__=__mul__

    def pop(self,i=-1):
        item=self[i]
        del self[i]
        return item
        
    def remove(self,x):    
        try:
            index = self.data.index(x)
        except ValueError:
            raise ValueError("not in list")
        self.pop(index)

    def max(self):
        max=self[0]
        for i in self:
          if i>max:
            max=i
        return max

    def min(self):
        min=self[0]
        for i in self:
          if i<min:
            min=i
        return min

    def sort(self, order = "asc"):
        if order == 'asc':
            self._A[:self._n] = sorted(self._A[:self._n])
        elif order == 'desc':
            self._A[:self._n] = sorted(self._A[:self._n], reverse=True)

    # ___________________________________________________________________________

    def union(self, b):
        common = UserDefinedDynamicArray()
        for item in self:
            if item not in b:
                common.append(item)
        for item in b:
            if item not in common:
                common.append(item)

        return common

    def intersect(self, b):
        common = UserDefinedDynamicArray()
    
        for item in self:
            if item in b:
                common.append(item)

        return common

def main():
    L1 = UserDefinedDynamicArray([1, 3, 5, 7, 9])
    L1.sort()
    L2 = UserDefinedDynamicArray([3, 4, 5, 6, 7])
    L2.sort()
    L3 = UserDefinedDynamicArray([2, 4, 6, 8, 10])
    L3.sort()

    L = L1.union(L2)
    L.sort()  # L should be the same as UserDefinedDynamicArray([1, 3, 4, 5, 6, 7, 9])
    print(L)

    L = L2.intersect(L3)
    L.sort()  # L should be the same as UserDefinedDynamicArray([4, 6])
    print(L)


if __name__ == '__main__':
    main()
