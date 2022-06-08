def solve(arr: list, n: int):
    if n == 1:
        return 0

    if arr[0] == 0:
        return -1

    jumps, steps_possible, max_reach = 1, arr[0], arr[0]

    for i in range(1, n):
        if(i == n-1):
            return jumps

        max_reach = max(max_reach, i+arr[i])
        steps_possible -= 1

        if(steps_possible == 0):
            jumps += 1
            if(i >= max_reach):
                return -1
            steps_possible = max_reach - i

    return jumps

test_cases = [[1, 4, 3, 2, 6, 7],[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]]
for i in test_cases:
    print("Test Result : ", solve(i, len(i))) 