'''7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, 
garanta que o sanduíche de 'pastrami' apareça na lista pelo menos três 
vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
Livro pg.183 pdf pg.166'''

pedidos_sanduiches = ['queijo', 'pastrami', 'atum', 'misto', 'pastrami', 'maionese de frango', 'pastrami',]
sanduiches_prontos = []

print("\nNo momento, não temos sanduíche de pastrami.")
while 'pastrami' in pedidos_sanduiches:
	pedidos_sanduiches.remove('pastrami')

while pedidos_sanduiches:
	sanduiche = pedidos_sanduiches.pop()
	
	print("\nPreparei um sanduíche de " + sanduiche + "!")
	sanduiches_prontos.append(sanduiche)
	
print("\nOs seguintes sanduíches foram preparados: ")
for sanduiche_pronto in sanduiches_prontos:
	print(sanduiche_pronto.title())
	
