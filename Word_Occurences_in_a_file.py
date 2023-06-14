# Program to multiply two matrices using nested loops

# take a 3x3 matrix
A = int(input("Enter a matrix in the form of lists"))
# take a 3x4 matrix
B = int(input("Enter 2nd matrix in the form of lists"))
	
result =result = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

	# iterating by column by B
	for j in range(len(B[0])):

		# iterating by rows of B
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]

for r in result:
	print(r)
