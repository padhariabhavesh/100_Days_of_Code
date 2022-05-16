# Decorator
def chees_and_buns(orogonal_fun):
	def wrap():
		print('I am upper bread')
		orogonal_fun()
		print('I am lower break')
	
	return wrap()


def chicken():
	print('I am roasted chieken')


chicken()
burger = chees_and_buns(chicken)

