'''7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
prontos, mostre uma mensagem que liste cada sanduíche preparado.
Livro pg.183 pdf pg.166
'''

pedidos_sanduiches = ['queijo', 'atum', 'misto', 'maionese de frango']
sanduiches_prontos = []

while pedidos_sanduiches:
	sanduiche = pedidos_sanduiches.pop()
	
	print("\nPreparei um sanduíche de " + sanduiche + "!")
	sanduiches_prontos.append(sanduiche)
	
print("\nOs seguintes sanduíches foram preparados: ")
for sanduiche_pronto in sanduiches_prontos:
	print(sanduiche_pronto.title())
	
