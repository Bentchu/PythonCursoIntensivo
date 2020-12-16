#5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma série de instruções if independentes que verifiquem se determinadas frutas estão em sua lista.
#• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
#• Escreva cinco instruções if. Cada instrução deve verificar se uma determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por exemplo, Você realmente gosta de bananas!

frutas = ['morango', 'pêssego', 'manga', 'laranja', 'banana', 'uva', 'limão', 'melão']
frutas_favoritas = ['morango', 'limão', 'pêssego', 'manga']

if 'pêssego' in frutas:
	print("Você gosta de pêssego!")
	
if 'jaca' in frutas:
	print("Você gosta de jaca!")
	
if 'laranja' in frutas:
	print("Você gosta de laranja!")
	
if 'uva' in frutas:
	print("Você gosta de uva!")
	
if 'manga' in frutas_favoritas:
	print("Você ama manga!")
	
if 'morango' in frutas_favoritas:
	print("Você ama morango!")
	
if 'jaca' in frutas_favoritas:
	print("Você ama jaca!")
	
