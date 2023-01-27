'''Cálculo de uso real para materiais de processo - Contagem Cíclica VW TBT.
v0.9 - Para Windows  - By Fábio Benteu - Taubaté 26/01/23
- Aprendi a usar funçoes, round e os.system('cls')'''

import sys, os

def calc_delta(uso_voy: float, uso_gol: float):
	return float(uso_voy/uso_gol)
		 	
def calc_uso_ac_gol(lb01: float, voyages: float, delta: float, gols: float):
	return float(lb01/((voyages*delta)+gols))
		
def calc_uso_ac_voy(uso_ac_gol: float, delta: float):
	return float(uso_ac_gol*delta)
	
def calc_dif_uso_gol(uso_ac_gol: float, uso_gol:float):
	return float(uso_ac_gol - uso_gol)
	
def calc_dif_uso_voy(uso_ac_voy: float, uso_voy:float):
	return float(uso_ac_voy - uso_voy)

opt = ''

while True:
	os.system('cls')
	lb01 = float(input('Entre as baixas para LB01 do material: '))
	gols = float(input('\nEntre o acumulado produzido de Gols: '))
	voyages = float(input('Entre o acumulado produzido de Voyages: '))
	uso_gol = float(input('\nEntre com uso de FCP para Gol: '))
	uso_voy = float(input('Entre com uso de FCP para Voyage: '))

	delta = calc_delta(uso_voy, uso_gol)
	
	uso_ac_gol = calc_uso_ac_gol(lb01, voyages, delta, gols)
	uso_ac_voy = calc_uso_ac_voy(uso_ac_gol, delta)
	uso_gol3 = round(uso_ac_gol, 3)
	uso_voy3 = round(uso_ac_voy, 3)
	
	dif_uso_gol = calc_dif_uso_gol(uso_ac_gol, uso_gol)
	dif_uso_voy = calc_dif_uso_voy(uso_ac_voy, uso_voy)
	dif_gol3 = round(dif_uso_gol, 3)
	dif_voy3 = round(dif_uso_voy, 3)

	'''print('Delta:' + str(delta) + '.')'''
    
	print('\nO uso por Gol foi de ' + str(uso_gol3) + '.')
	print('O uso por Voyage foi de ' + str(uso_voy3) + '.')
	print('\nA diferença de uso do Gol foi de: ' + str(dif_gol3) + '.')
	print('A diferença de uso do Voyage foi de: ' + str(dif_voy3) + '.')
	
	opt = input('\nNovo cálculo (s/n)? ')
	if opt == 'n':
		sys.exit()
		
