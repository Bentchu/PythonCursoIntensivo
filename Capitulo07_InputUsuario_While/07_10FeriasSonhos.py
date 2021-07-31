'''7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete.
Livro pg.183 pdf pg.167
'''

respostas = {}

enquete_active = True

while enquete_active:
	nome = input("\nQual é seu nome? ") 
	resposta = input("Qual lugar gostaria de passar suas férias algum dia? ")
	respostas[nome] = resposta
	
	repeat = input("Gostaria de deixar outra pessoa responder? (yes/ no) ") 
	if repeat == 'no':
		enquete_active = False
		
print("\n--- resultado da Enquete---")
for nome, resposta in respostas.items(): 
	print(nome + " gostaria de visitar " + resposta + ".")
