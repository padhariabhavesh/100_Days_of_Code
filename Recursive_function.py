# Calculate Factorial: Recursive
print('x' * 20)


def recursivefun(n):
	if n <= 1:
		return 1
	else:
		a = n * recursivefun(n - 1)
		return a


for i in range(1, 10):
	print(i, recursivefun(i))