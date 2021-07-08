'''6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
bastante para poderem ser estendidos de várias maneiras. Use um dos
programas de exemplo deste capítulo e estenda-o acrescentando novas chaves
e valores, alterando o contexto do programa ou melhorando a formatação da
saída.
pg164 papel pg150 pdf
'''

cities = { 'Macaé' : {'País' : 'Brasil', 'Estado' : 'Rio de Janeiro', 'População' : '261500', 'Perfil' : 'Industrial'},
			'Pune' : {'País' : 'Índia', 'Estado' : 'Maharashtra', 'População' : '7400000', 'Perfil' : 'Comercial'},
			'Hamburg' :	{'País' : 'Alemanha', 'Estado' : 'Cidade Livre', 'População' : '1800000', 'Perfil' : 'Turismo e Portuário'},
			'Dubai' : {'País' : 'Emirados Árabes Unidos', 'Estado' : 'N/A', 'População' : '3331000', 'Perfil' : 'Turismo e Comércio'},
		 } 

for cidade, dados in cities.items():
	print("\nCidade: " + cidade.title())
	print("- País: " + dados['País'].title())
	print("- Estado: " + dados['Estado'].title())
	print("- População: " + dados['População'].title())
	print("- Perfil: " + dados['Perfil'].title())
