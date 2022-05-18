# Initialization function
class map():
	def __init__(self, material):
		self.material = material
		print(f'I build {material}')
	
	def adder(self):
		x = 2 + 2
		return x


house1 = map('New material1')
house2 = map('New material2')
house3 = map('New material3')
house4 = map('New material4')