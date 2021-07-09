'''7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao 
usuário quantas pessoas estão em seu grupo para jantar. Se a resposta 
for maior que oito, exiba uma mensagem dizendo que eles deverão esperar 
uma mesa. Caso contrário, informe que sua mesa está pronta.
livro pg 171 pdf pg 156
'''
lugares = input("Quantas pessoas deseujam jantar? ")
lugares = int(lugares)

if lugares > 8:
	print("\nSinto muito, mas é necessário esperar por uma mesa.")
else: 
	print("\nSua mesa já está pronta!")
