# Function to check if strings 'X' and 'Y' are interleaving of 'S' or not
def isInterleaving(A, B, C):
	A, B, C = X, Y, S
	M, N = len(X), len(Y)

	# base case: length of given strings doesn't match
	if M + N != len(S):
		return False

	# Create a lookup table T[][] to store solution to already computed
	# subproblems. T[i][j] is true when `S[0…i+j-1]` is an interleaving
	# of `X[0…i-1]` and `Y[0…j-1]`
	T = [[False for x in range(N + 1)] for y in range(M + 1)]

	# fill the lookup table in a bottom-up manner
	for i in range(0, M + 1):
		for j in range(0, N + 1):

			if i == 0 and j == 0:		# both strings are empty
				T[i][j] = True

			# if the current char of 'S' matches the current char of both 'A' and 'B'
			elif i and j and X[i - 1] == S[i + j - 1] and Y[j - 1] == S[i + j - 1]:
				T[i][j] = T[i - 1][j] or T[i][j - 1]

			# if the current char of 'X' matches with the current char of 'S'
			elif i and X[i - 1] == S[i + j - 1]:
				T[i][j] = T[i - 1][j]

			# if the current char of 'Y' matches with the current char of 'S'
			elif j and Y[j - 1] == S[i + j - 1]:
				T[i][j] = T[i][j - 1]

	# T[M][N] stores the result
	return T[M][N]


if __name__ == '__main__':

	X = 'ABC'
	Y = 'ACD'
	S = 'ACDABC'

	print(isInterleaving(X, Y, S))
