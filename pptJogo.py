'''Jogo Pedra, Papel, Tesoura , de "Automate the boring stuff with Python"
by Al Weigart. 16/01/23'''

import random, sys, time

print('Pedra, Papel, Tesoura')

vencidas = 0
empates = 0
perdidas = 0

while True:
	print('%s Vencidas, %s Perdidas, %s Empates' % (vencidas, perdidas, empates))
	while True:
		print('Entre com sua escolha: (p)edra, p(a)pel, (t)esoura ou (q)abandonar')
		playerEscolha = input()
		if playerEscolha == 'q':
			sys.exit()
		if playerEscolha == 'p' or playerEscolha == 'a' or playerEscolha == 't':
			break
		print('Digite p, a, t ou q.')
		
	if playerEscolha == 'p':
		print('Pedra contra...')
	elif playerEscolha == 'a':
		print('Papel contra...')
	elif playerEscolha == 't':
		print('Tesoura contra...')
		
	randomNumero = random.randint(1,3)
	time.sleep(3)
	if randomNumero == 1:
		computerEscolha = 'p'
		print('Pedra!')
	elif randomNumero	== 2:
		computerEscolha = 'a'
		print('Papel!')
	elif randomNumero	== 3:
		computerEscolha = 't'
		print('Tesoura!')
		
	if playerEscolha == computerEscolha:
		print('É um empate')
		empates = empates + 1
	elif playerEscolha == 'p' and computerEscolha == 't':
		print('Você ganhou!')
		vencidas = vencidas + 1
	elif playerEscolha == 't' and computerEscolha == 'a':
		print('Você ganhou!')
		vencidas = vencidas + 1
	elif playerEscolha == 'a' and computerEscolha == 'p':
		print('Você ganhou!')
		vencidas = vencidas + 1
	elif playerEscolha == 'p' and computerEscolha == 'a':
		print('Você perdeu!')
		perdidas = perdidas + 1
	elif playerEscolha == 't' and computerEscolha == 'p':
		print('Você perdeu!')
		perdidas = perdidas + 1
	elif playerEscolha == 'a' and computerEscolha == 't':
		print('Você perdeu!')
		perdidas = perdidas + 1
