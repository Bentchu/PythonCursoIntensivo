'''6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações
sobre cada cidade e inclua o país em que a cidade está localizada, a
população aproximada e um fato sobre essa cidade. As chaves do dicionário
de cada cidade devem ser algo como country, population e fact. Apresente o
nome de cada cidade e todas as informações que você armazenou sobre ela.
pg 164 papel pg 150 pdf
01/06/21'''

cities = { 'Taubaté' : { 'País' : 'Brasil', 'População' : '300000', 'Perfil' : 'Industrial'},
			'Tremembé' : { 'País' : 'Brasil', 'População' : '40000', 'Perfil' : 'Turismo'},
			'São Luiz do Paraitinga' :	{ 'País' : 'Brasil', 'População' : '20000', 'Perfil' : 'Agropecuária'},
		 } 

for cidade, dados in cities.items():
	print("\nCidade: " + cidade.title())
	print("- País: " + dados['País'].title())
	print("- População: " + dados['População'])
	print("- Perfil: " + dados['Perfil'].title())
