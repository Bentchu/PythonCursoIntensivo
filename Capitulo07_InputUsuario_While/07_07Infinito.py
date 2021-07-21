'''falta descrição'''

idade = "\nQual a idade da pessoa que deseja o ingresso?  "

idade = input(idade)
idade = int(idade)

while idade < 100:
	
	if idade < 3:
		print ("\nO ingresso para menores de 3 anos é gratuito.")
	
	elif idade < 12:
		print ("\nO ingresso para clientes de 3 a 12 anos custa 10 dólares.")
		
	else:
		print ("\nO ingreso para maiores de 12 anos custa 15 dólares.")
