matrix = [['x','0','x'], ['x', 'x', 'x'], ['0', 'x','0']]
def check_rows(matrix):
	for i in matrix:
		if i == ['x','x','x'] or i == ['0','0','0']:
			return True
			pass
	return False

print check_rows(matrix)

def check_columns(matrix):
	for col in range(0,3):
		if [matrix[0][col], matrix[1][col], matrix [2][col]] == ['x','x','x'] or [matrix[0][col], matrix[1][col], matrix [2][col]] == ['0','0','0']:
		#if [matrix[0][col] ==[matrix[1][col] == matrix [2][col]]:
			return True
			pass
	return False
print check_columns(matrix)

def check_diags(matrix):
	for i in range(0,2):
		if matrix[0][i] == matrix[1][i+1] == matrix[2][i+2] or matrix[0][i+1] == matrix[1][i] == matrix[2][i-1]:
			return True
			pass
	return False
print check_diags(matrix)

		




		




