'''falta descrição'''

prompt = "\nQual ingrediente deseja em sua pizza?. "
prompt += "\nEntre 'quit' para encerrar o programa.     "

active = True
while active:
	ingrediente = input(prompt)
	
	if ingrediente == 'quit':
		active = False
	else:
		print("\nAdicionarei " + ingrediente.title() + " à sua pizza!")
