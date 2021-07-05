#6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
#cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
#• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
#pelo Egito.
#• Use um laço para exibir o nome de cada rio incluído no dicionário.
#• Use um laço para exibir o nome de cada país incluído no dicionário.
#24/05/21

rios = { 'Orenoco' : 'Venezuela',
		'Amarelo' : 'China',
		'La Plata' : 'Argentina' }
		
for rio, pais in rios.items():
	print ("O rio " + rio.title() + " corre na " + pais.title() + ".")
	
for nome, lugar in rios.items():
	print(nome)
	print (lugar)
	
