'''Arazena informações sobre uma pizza que está sendo pedida
28/05/21'''

pizza={
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
	
#resume o pedido

print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
	
for topping in pizza ['toppings']:
	print("\t" + topping)
	
