def solve(X: int):
    x = " ".join(str(X))
    x = list(x.split(' '))
    for i in range(len(x)-1):
        first_num = int(x[i])
        next_num = int(x[i+1])

        if first_num+1 == next_num or first_num-1 == next_num:
            continue
        else:
            if first_num > next_num:
                diff = first_num - next_num
                if next_num != 0:
                    x[i+1] = '{}'.format(next_num + (diff-1))
                else:
                    x[i+1] = '{}'.format(next_num + (diff-1))
                    temp = x[i]
                    x[i] = x[i+1]
                    x[i+1] = temp
                continue
            elif first_num < next_num:
                diff = next_num - first_num
                if next_num != 0:
                    x[i+1] = '{}'.format(next_num - (diff-1))
                else:
                    x[i+1] = '{}'.format(next_num - (diff-1))
                    temp = x[i]
                    x[i] = x[i+1]
                    x[i+1] = temp
                continue

    return int(''.join(x))

# -----------------------------
# jumping_numbers = [45676, 212, 121, 123, 210, 212, 232, 234, 321, 323, 343, 345, 432, 434, 454, 456, 543, 545, 565, 567, 654, 656, 676, 678, 765, 767, 787, 789, 876]
# for i in jumping_numbers:
#     if solve(i) == i:
#         print('test passed !')
#     else:
#         print('test failed at {}'.format(i))
# --------------------------------
import unittest

class test_cases(unittest.TestCase):

    def test_jumping_numbers(self):
        
        self.assertEqual(solve(69),67)
        self.assertEqual(solve(3892),3454)
        self.assertEqual(solve(235),234)
        self.assertEqual(solve(10),10)
        self.assertEqual(solve(4343456),4343456)
        self.assertEqual(solve(67),67)

if __name__ == '__main__' :
    unittest.main()