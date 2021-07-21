'''falta descrição
loop infinito
tratar var 'idade' separado quando fôr string ou numérica?'''

idade = "\nQual a idade da pessoa que deseja o ingresso?  "
idade += "\nEntre 'quit' para encerrar o programa.     "

idade = input(idade)

active = True

while active:
	
	if idade == 'quit':
		active = False
	
	idade = int(idade)
	
	if idade < 3:
		print ("\nO ingresso para menores de 3 anos é gratuito.")
		
	elif idade < 12:
		print ("\nO ingresso para clientes de 3 a 12 anos custa 10 dólares.")
		
	else :
		print ("\nO ingresso para maiores de 12 anos custa 15 dólares.")

