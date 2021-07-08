'''6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.
pg164 papel pg150 pdf
01/06/2021'''

pessoas = {'Alessandra': '5', 
    'Helmer': '10',
    'Timóteo': '42',
    'Maria': '3',
    'Vanda': '1'}
    
for pessoa, numeros in pessoas.items():
    
	print("Número favorito de " +  pessoa + " é ou são: " + numeros + ".")

