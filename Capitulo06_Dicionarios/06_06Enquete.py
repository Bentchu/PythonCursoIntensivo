"""#6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
#• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
#favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
#estão.
#• Percorra a lista de pessoas que devem participar da enquete. Se elas já
#tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
#responder. Se ainda não participaram da enquete, apresente uma mensagem
#convidando-as a responder.
#24/05/21"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'john': 'fortran',
    'douglas': 'dbase',
    'penny': 'c'
    }
 
enquete = ['jen', 'sarah', 'phil', 'andrea', 'klaus']

for nome in enquete:
	if nome in favorite_languages:
		print("\nObrigado por participar, " + nome.title() + "!")
		
	else:
		print("\n" + nome.title() + ", por favor, responda a pesquisa!")

		
