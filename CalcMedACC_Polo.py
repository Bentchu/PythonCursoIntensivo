'''Cálculo de uso real para materiais de processo *Polo* - Contagem Cíclica VW TBT.
v0.9 - Para Windows  - By Fábio Benteu - Taubaté 31/01/23.
- Aprendi a usar funçoes, round e os.system('cls')'''

import sys, os, time

def calc_delta(uso_pa: float, uso_track: float):
	return float(uso_pa/uso_track)
		 	
def calc_uso_ac_track(lb01: float, pas: float, delta: float, tracks: float):
	return float(lb01/((pas*delta)+tracks))
		
def calc_uso_ac_pa(uso_ac_track: float, delta: float):
	return float(uso_ac_track*delta)
	
def calc_dif_uso_track(uso_ac_track: float, uso_track:float):
	return float(uso_ac_track - uso_track)
	
def calc_dif_uso_pa(uso_ac_pa: float, uso_pa:float):
	return float(uso_ac_pa - uso_pa)

opt = ''

print('Cálculo de uso real para materiais de processo *Polo* - Contagem Cíclica VW TBT.')
print('v0.9 - Windows  - By Fábio Benteu - Taubaté 31/01/23')
time.sleep(3)

while True:
	os.system('cls')
	lb01 = float(input('Entre as baixas para LB01 do material: '))
	tracks = float(input('\nEntre o acumulado produzido de Tracks: '))
	pas = float(input('Entre o acumulado produzido de Polo PA: '))
	uso_track = float(input('\nEntre com uso de FCP para Track: '))
	uso_pa = float(input('Entre com uso de FCP para Polo PA: '))
	
	if uso_track > uso_pa:
		print('Uso Track maior que uso PA. Situação não atendida!')
		break
	
	delta = calc_delta(uso_pa, uso_track)
	
	uso_ac_track = calc_uso_ac_track(lb01, pas, delta, tracks)
	uso_ac_pa = calc_uso_ac_pa(uso_ac_track, delta)
	uso_track3 = round(uso_ac_track, 3)
	uso_pa3 = round(uso_ac_pa, 3)
	
	dif_uso_track = calc_dif_uso_track(uso_ac_track, uso_track)
	dif_uso_pa = calc_dif_uso_pa(uso_ac_pa, uso_pa)
	dif_pa3 = round(dif_uso_track, 3)
	dif_track3 = round(dif_uso_pa, 3)

	'''print('Delta:' + str(delta) + '.')'''
    
	print('\nO uso por Track foi de ' + str(uso_track3) + '.')
	print('O uso por Polo PA foi de ' + str(uso_pa3) + '.')
	print('\nA diferença de uso do Track foi de: ' + str(dif_track3) + '.')
	print('A diferença de uso do Polo PA foi de: ' + str(dif_pa3) + '.')
	
	opt = input('\nNovo cálculo (s/n)? ')
	if opt == 'n':
		print('***Até Logo!***')
		sys.exit()
		
