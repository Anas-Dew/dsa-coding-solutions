def generate(rowIndex: int):
        master = [[1]]
        for i in range(rowIndex):
            temp = [0] + master[-1] + [0]
            row = []
            for j in range(len(master[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            master.append(row)
        return master[rowIndex]

numRows = 3
print(generate(numRows))