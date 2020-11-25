my_foods = ['Pizza', 'Donut', 'Bolo de cenoura']
friend_foods = my_foods[:]

my_foods.append('Paçoca')
friend_foods.append('Rabada')

print("Minhas comidas favoritas são:\n")
for food in my_foods:
	print(food.title() + "!\n")
	
print("As comidas favoritas do João são:\n")
for friend_food in friend_foods:
	print(friend_food.title() + "!\n")

