'''7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
7.5 que faça o seguinte, pelo menos uma vez: • use um teste condicional na
instrução while para encerrar o laço; • use uma variável active para controlar
o tempo que o laço executará; • use uma instrução break para sair do laço
quando o usuário fornecer o valor 'quit'.
livro pg.179 pdf pg.163

pra quê o active?'''

active = True

while active:
	
	idade = "\nQual a idade da pessoa que deseja o ingresso?  "
	idade += "\nEntre 'quit' para encerrar o programa.     "

	idade = input(idade)

	if idade == 'quit':
		break
	
	idade = int(idade)
	
	if idade < 3:
		print ("\nO ingresso para menores de 3 anos é gratuito.")
		
	elif idade < 12:
		print ("\nO ingresso para clientes de 3 a 12 anos custa 10 dólares.")
		
	else :
		print ("\nO ingresso para maiores de 12 anos custa 15 dólares.")

