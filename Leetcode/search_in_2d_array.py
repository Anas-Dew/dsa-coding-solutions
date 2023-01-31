class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        that_row = 0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target :
                break
            else :
                that_row += 1
        try:
            if target in matrix[that_row]:
                return True
        except:
            return False

if __name__ == "__main__" :
    test = Solution()
    print(test.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
    print(test.searchMatrix(matrix=[[1]], target=2))
    # a = [[1]]
    # print(a[0][-1])