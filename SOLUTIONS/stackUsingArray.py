class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        # return self.arr
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.arr == None:
            return -1
        self.arr.remove(self.arr[-1])
        return self.arr

# -----------------------------------
import unittest

class test_cases(unittest.TestCase):

    def test_mystack(self):
        s = MyStack()
        self.assertEqual(s.push(2), None)
        self.assertEqual(s.push(4), None)
        self.assertEqual(s.push(78), None)
        self.assertEqual(s.pop(), [2,4])

if __name__ == '__main__' :
    unittest.main()