'''6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
pg164 livro pg149 pdf
31/05/21'''


xuxu = 	{ 
		'cão' : 'james', 
		}
		
charlie = 	{ 
		'gato' : 'erasmo',
		}
		
stuka = { 
		'canário' : 'flávio',
		}
		
skye = { 
		'jabuti' : 'alessandra', 
		}


pets = [xuxu, charlie, stuka, skye]

for pet in pets:
	print(pet)
