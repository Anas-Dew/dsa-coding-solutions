def feb(n):
    if n == 0 or n == 1 :
        return n
    return feb(n-2) + feb(n-1)

def factorial(n):
    if n == 2 or n == 1:
        return n
    if 0 >= n:
        return -1

    return n * factorial(n-1)
# for n = 3
    # it will check wheather n == 2 or == 1 if yes -> return, else return n and fac of n-1
    # but what is fac of n-1
    # then second iteration
    # is n-1 == 2 or == 1
    # >>> 3-1 == 2 and it's yes so return n means 2
    # now this iteration will return n * fac (n-1) >> 2
    # >>>>>>>> 3 * 2 == 6 
if __name__ == "__main__":
    # print(feb(6))
    print(factorial(3))