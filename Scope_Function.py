# Local and Global Scope in function

# Global Scope
x = 1


def fun():
	# Local Scope
	# global x
	# x = 1
	def fun2():
		print(x)
	
	fun2()


fun()

print(x)