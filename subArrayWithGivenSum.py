import time
def solveA(array: list, length_of_list: int, sumof: int):
    indexes = []
    count = 0
    step = 0
    for k in range(length_of_list):
        for i in range(step, length_of_list):
            count+=array[i]
            indexes.append(i+1)
            if count == sumof:
                return [indexes[0],indexes[-1]]
        step+=1
        count = 0
        indexes = []
    return [-1]

# --------------------THIS IS MORE FAST 0.73SEC-------
def solveB(array: list, length_of_list: int, sumof: int):
    ini = 0
    fin = 0
    i = 0
    st = 0
    while(i<length_of_list):
                st = st + array[i]
                fin = i
                if(st == sumof):
                    return [ini+1, fin+1]
                elif(st > sumof):
                    st = st - array[ini] - array[fin]
                    ini+=1
                else:
                    i+=1
            
    return [-1]

# -----------------------------------------------------

array = [1,2,3,7,5]
length_of_list = 5
sumof = 12


start = time.time()
print(solveB(array, length_of_list, sumof))
end = time.time()

print('Total time taken : ', end - start)