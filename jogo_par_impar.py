'''Jogo de par ou ímpar

Histórico:
11/07/21  - aprender a importar biblioteca random
'''

import random

continuar=1

while continuar == 1:
	print("Número aleatório gerado:", random.randint(1,2))
	continuar = input("Gerar novamente?\n1.Sim\n0.Não\n")
	continuar = int(continuar)
