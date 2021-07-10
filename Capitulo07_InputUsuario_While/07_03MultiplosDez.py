'''7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, 
informe se o número é múltiplo de dez ou não.
livro pg 171 pdf pg 156
'''
numero = input("Entre um número, e eu lhe direi se este é múltiplo de dez: ")
numero = int(numero)

if numero % 10 == 0:
	print("\nO número " + str(numero) + " é múltiplo de dez.")
	
else:
	print("\nO número " + str(numero) + " não é múltiplo de dez.")
	
