'''Preimeiro exemplo de flag'''

prompt = "\nMe diga algo, e eu repetirei de volta à você. "
prompt += "\nEntre 'quit' para encerrar o programa.     "

active =True
while active:
	mensagem = input(prompt)
	
	if mensagem == 'quit':
		active = False
	else:
		print(mensagem)
