#Curso Intensivo de Python - Eric Matthes - 4.11 pg.108
pizzas=['Margherita','Calabreza','Cinco Queijos','Atum','Lombo']
friend_pizzas = pizzas[:]
pizzas.append('Muzzarella')
friend_pizzas.append('Rúcula')
for pizza in pizzas:
		print("Gosto de pizza de " + pizza.title() + "!\n")
for friend_pizza in friend_pizzas:
		print("O João gosta de pizza de " + friend_pizza.title() + "!\n")
		
print("Nós realmente amamos pizza!")
