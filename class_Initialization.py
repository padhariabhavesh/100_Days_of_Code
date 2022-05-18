# Class  Exercise

class kattle():
	# Universal Attribute
	# Class Atribute
	power_src = 'Electricity'
	
	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False
	
	def switch(self):
		self.on = True


kenwood = kattle('Kenwood', 10)
hamilton = kattle('Hamilton', 20)

# print(kenwood.make)
# print(kenwood.on)
# kenwood.switch()
# print(kenwood.on)

print(hamilton.power_src)
print(kenwood.power_src)