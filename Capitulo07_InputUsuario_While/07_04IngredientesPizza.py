'''7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
livro pg.178 pdf pg.163'''

prompt = "\nQual ingrediente deseja em sua pizza?. "
prompt += "\nEntre 'quit' para encerrar o programa.     "

active = True
while active:
	ingrediente = input(prompt)
	
	if ingrediente == 'quit':
		active = False
	else:
		print("\nAdicionarei " + ingrediente.title() + " à sua pizza!")
