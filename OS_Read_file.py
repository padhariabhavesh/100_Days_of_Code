import os

list_os = os.walk('D:\\Practice\\Python')

for root, direct, files in list_os:
	# print(root)
	# for i in direct:
	#  print(i)
	for j in files:
		if 'Function.py' in j:
			print(j)
	# print(j)