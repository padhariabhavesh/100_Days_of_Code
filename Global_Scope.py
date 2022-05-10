# Global Exercise



clothes = 'dirty_clothes'


def washingmachine(cleanclothes):
	global clothes
	clothes = cleanclothes
	print(clothes)


print(clothes)
washingmachine('Clean clothes')
print(clothes)