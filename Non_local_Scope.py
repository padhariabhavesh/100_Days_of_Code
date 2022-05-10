# Non Local Key word
global scope


def fun1():
	# enclosing function/scope
	def fun2():
		# neseted function
		# local scope
		print(2)
	
	fun2()
	print(1)


fun1()
print('** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **')
# Exercise non local

#
# def fun1():
# 	def fun2():
# 		print(1)
# 	fun2()
# 	print(2)