# Dictionaries
car = {
	'model': 'suzuki',
	'year': [2006, 2003, 2006],
	'color': ('black', 'red'),
	'docs': {'original': 'yes', 'duplicate': 'No'}
}

# # # print(dict_a['key4'])
# # print(dict_a.get('key4'))
# print(car['model'])
#
# print(car['color'][1])
# print(car['docs']['duplicate'])

car['model'] = 'toyota'
car['tyers'] = 'No'
print(car.items())
# a,b,c,d,e=car.items()
a, b, c, d, e = car.keys()
print(car.keys())
print(a)
print(b)
print(c)
print(d)
print(e)
print(car.values())
q, w, e, t, y = car.values()
print(q)
print(w)
print(e)
print(t)
print(y)
# print(car)
new_doct = dict([('model', 'toyota'), ('year', [2006, 2003, 2006]), ('color', ('black', 'red'))])

print(new_doct)
# new_doct.pop('model')
# print(new_doct)
# new_doct.popitem()
# print(new_doct)

del new_doct

print(new_doct)



