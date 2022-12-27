def generate(numRows: int):
        master = [[1]]
        for i in range(numRows - 1):
            temp = [0] + master[-1] + [0]
            row = []
            for j in range(len(master[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            master.append(row)
            
        return master

numRows = 5
print(generate(numRows))
# a = [[1],[1]]
# print(a[0])