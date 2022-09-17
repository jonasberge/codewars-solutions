# 3 kyu - How many are smaller than me II?
# https://www.codewars.com/kata/56a1c63f3bc6827e13000006

class Tree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self._left_count = 0
        self._amount = 1
    
    def insert(self, value, _left_carry=0):
        if value is None:
            raise ValueError()
        
        if self.value is None:
            self.value = value
            self._amount = 1
            return _left_carry
        
        if value == self.value:
            self._amount += 1
            return self._left_count + _left_carry
        
        if value < self.value:
            if self.left is None:
                self.left = Tree()
            self._left_count += 1
            return self.left.insert(value, _left_carry)
        
        if value > self.value:
            if self.right is None:
                self.right = Tree()
            _left_carry += self._left_count
            _left_carry += self._amount
            return self.right.insert(value, _left_carry)
        
        return 0
        

def smaller(arr):
    
    tree = Tree()
    output = [0] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        value = arr[i]
        left_count = tree.insert(value)
        output[i] = left_count
    
    return output
