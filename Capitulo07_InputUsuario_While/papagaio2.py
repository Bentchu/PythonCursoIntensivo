prompt = "\nMe diga algo, e eu repetirei de volta à você. "
prompt += "\nEntre 'quit' para encerrar o programa.     "

mensagem = ''
while mensagem != 'quit':
	mensagem = input(prompt)
	print(mensagem)
