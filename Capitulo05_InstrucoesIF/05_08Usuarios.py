#5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, 
#incluindo o nome 'admin'. Suponha que você esteja escrevendo um código 
#que exibirá uma saudação a cada usuário depois que eles fizerem login 
#em um site.
#Percorra a lista com um laço e mostre uma saudação para cada usuário: 
#• Se o nome do usuário for 'admin', mostre uma saudação especial, 
#por exemplo, Olá admin, gostaria de ver um relatório de status? 
#• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado
# por fazer login novamente.

usuarios = [ 'José', 'Pedro', 'João', 'Admin', 'Mateus', 'Tiago']
usuario = 'Tanga Frouxa'

if usuario == 'Admin':
	print("Olá, Admin! Gostaria de ver log?")

elif usuario in usuarios:
	print("Olá, " + usuario + "!")
	
else:
	print("Usuário não encontrado!")

