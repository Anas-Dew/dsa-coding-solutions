def solve(array : list) : 
    array.sort()
    return array
# ---------------------------------------
import unittest
class test_cases(unittest.TestCase):

    def test(self):
        self.assertEqual(solve([1,2,0,2,0,1,1]),[0,0,1,1,1,2,2])
        self.assertEqual(solve([1,2,0]),[0,1,2])
        self.assertEqual(solve([2,1,2,1,0]),[0,1,1,2,2])

if __name__ == '__main__' :
    unittest.main()