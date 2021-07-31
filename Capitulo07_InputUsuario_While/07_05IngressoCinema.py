'''7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema.
livro pg.179 pdf pg.163'''

idade = "\nQual a idade da pessoa que deseja o ingresso?  "

idade = input(idade)
idade = int(idade)

if idade < 3:
	print ("\nO ingresso para menores de 3 anos é gratuito.")
	
elif idade < 12:
	print ("\nO ingresso para clientes de 3 a 12 anos custa 10 dólares.")
		
else:
	print ("\nO ingresso para maiores de 12 anos custa 15 dólares.")
