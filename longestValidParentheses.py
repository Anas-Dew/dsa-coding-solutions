def solve(S: str):
        stack, ans = [-1], 0
        for i in range(len(S)):
            if S[i] == '(': stack.append(i)
            elif len(stack) == 1: stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans



test_cases = ['((()', ')()())', '(((((', '(((()()))())', ')))))(']
for i in test_cases:
    print(solve(i), end=' ')