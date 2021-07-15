prompt = "\nPor favor, entre o nome de uma cidade que você já visitou: "
prompt += "\nEntre 'quit' quando terminar.     "


while True:
	cidade = input(prompt)
	
	if cidade == 'quit':
		break
	else:
		print("Eu adoraria ir para " + cidade.title() + "!")
