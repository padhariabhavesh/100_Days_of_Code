a = [10, 20, 15, 5, 35]
num = 20




c = a[2] + a[3]
print(c)

def sum():
	if c == num:
		print('match')
	else:
		print('not match')
		
sum()

# Important  Code
# Naive method to find a pair in a list with the given sum
def findPair(nums, target):
	# consider each element except the last
	for i in range(len(nums) - 1):
		
		# start from the i'th element until the last element
		for j in range(i + 1, len(nums)):
			
			# if the desired sum is found, print it
			if nums[i] + nums[j] == target:
				print('Pair found', (nums[i], nums[j]))
				return
	
	# No pair with the given sum exists in the list
	print('Pair not found')


if __name__ == '__main__':
	nums = [8, 7, 2, 5, 3, 1]
	target = 10
	
	findPair(nums, target)