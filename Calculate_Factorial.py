# Function Exercise:
# Calculate Factorial
def fact_fun(n):
	result = 1
	for n in range(2, n + 1):
		result = result * n
	return result


for i in range(1, 10):
	print(i, fact_fun(i))