def solve(S : str):
    temp_list = S.split('.')
    temp_list.reverse()
    return '.'.join(temp_list)

# ---------------------------
test_cases = ['i.like.this.program.very.much','pqr.mno','star.this.repo.and.have.fun']
for i in test_cases:
    print(solve(i))