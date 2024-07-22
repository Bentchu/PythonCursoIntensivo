'''Cálculo de uso real para materiais de processo - Contagem Cíclica VW TBT.
v0.9 - Para Windows  - By Fábio Benteu - Taubaté 26/01/23
- Aprendi a usar funçoes, round e os.system('cls')'''

import sys, os, time

def calc_delta(uso_suv: float, uso_pol: float):
	return float(uso_suv/uso_pol)
		 	
def calc_uso_ac_pol(lb01: float, SUVs: float, delta: float, Polos: float):
	return float(lb01/((SUVs*delta)+Polos))
		
def calc_uso_ac_suv(uso_ac_pol: float, delta: float):
	return float(uso_ac_pol*delta)
	
def calc_dif_uso_pol(uso_ac_pol: float, uso_pol:float):
	return float(uso_ac_pol - uso_pol)
	
def calc_dif_uso_suv(uso_ac_suv: float, uso_suv:float):
	return float(uso_ac_suv - uso_suv)

opt = ''

print('Cálculo de uso real para materiais de processo *Polo* & *A0 SUV* - Contagem Cíclica VW TBT.')
print('v0.9 - Windows  - By Fábio Benteu - Taubaté 02/02/24')
time.sleep(3)

while True:
	os.system('cls')
	lb01 = float(input('Entre as baixas para LB01 do material: '))
	Polos = float(input('\nEntre o acumulado produzido de Polos: '))
	SUVs = float(input('Entre o acumulado produzido de SUVs: '))
	uso_pol = float(input('\nEntre com uso de FCP para Polo: '))
	uso_suv = float(input('Entre com uso de FCP para SUV: '))

	delta = calc_delta(uso_suv, uso_pol)
	
	uso_ac_pol = calc_uso_ac_pol(lb01, SUVs, delta, Polos)
	uso_ac_suv = calc_uso_ac_suv(uso_ac_pol, delta)
	uso_pol3 = round(uso_ac_pol, 3)
	uso_suv3 = round(uso_ac_suv, 3)
	
	dif_uso_pol = calc_dif_uso_pol(uso_ac_pol, uso_pol)
	dif_uso_suv = calc_dif_uso_suv(uso_ac_suv, uso_suv)
	dif_pol3 = round(dif_uso_pol, 3)
	dif_suv3 = round(dif_uso_suv, 3)

	'''print('Delta:' + str(delta) + '.')'''
    
	print('\nO uso por Polo foi de ' + str(uso_pol3) + '.')
	print('O uso por SUV foi de ' + str(uso_suv3) + '.')
	print('\nA diferença de uso do Polo foi de: ' + str(dif_pol3) + '.')
	print('A diferença de uso do SUV foi de: ' + str(dif_suv3) + '.')
	
	opt = input('\nNovo cálculo (s/n)? ')
	if opt == 'n':
		sys.exit()
		
