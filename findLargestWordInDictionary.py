def solve(s : str, d : list):
    s_list = list(s)
    largest_word_list = []
    for i in d:
        signal = False
        for each in list(i):
            if each in s_list:
                signal = True
            else:
                signal = False
                break
        if signal == True:
            largest_word_list.append(i)
    return max(largest_word_list, key=len)
    
# failed for some big input from gfg.
# ------------------------------------------------------
test_cases = [["ale", "apple", "monkey", "plea"],["a", "b", "c"]]
test_cases_str = "abpcplea"

for i in test_cases:
    print(solve(test_cases_str, i))