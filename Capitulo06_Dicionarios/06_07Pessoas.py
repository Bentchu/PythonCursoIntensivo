'''6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista
de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa.
pg163 livro pg 149 pdf
31/05/21'''

pessoa_1 = {'primeiro_nome': 'jeca', 
			'sobrenome': 'tatu',
			'idade': '129',
			'cidade': 'tremembé'
		}
    
pessoa_2 = {'primeiro_nome': 'josé', 
			'sobrenome': 'da couves',
			'idade': '99',
			'cidade': 'pindamonhangaba'
		}
    
pessoa_3 = {'primeiro_nome': 'Maria', 
			'sobrenome': 'Gasolina',
			'idade': '525',
			'cidade': 'natividade da Serra'
		}

pessoas = [pessoa_1, pessoa_2, pessoa_3]

for pessoa in pessoas:
		print(pessoa)
   
