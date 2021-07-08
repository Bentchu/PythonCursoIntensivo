'''6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três
lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
interessante, peça a alguns amigos que nomeiem alguns de seus lugares
favoritos. Percorra o dicionário com um laço e apresente o nome de cada
pessoa e seus lugares favoritos.
 pg 164 papel pg149 pdf'''
 
favorite_places = {
					'Flávio' : 'Minha Casa', 
					'Alessandra' : 'Santo Antônio, Campos, Ubatuba',
					'Helmer' : 'GTA online, Minecraft'
					}
					
for nome, lugar in favorite_places.items():
	print("O lugar favorito de " + nome + " é:" + lugar)
 
 
