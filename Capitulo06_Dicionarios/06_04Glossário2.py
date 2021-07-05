#6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário 
#com um laço, limpe o código do Exercício 6.3 (página 148), 
#substituindo sua sequência de instruções print por um laço que 
#percorra as chaves e os valores do dicionário. Quando tiver certeza 
#de que seu laço funciona, acrescente mais cinco termos de Python ao 
#seu glossário. Ao executar seu programa novamente, essas palavras 
#e significados novos deverão ser automaticamente incluídos na saída.
#24/05/21. Pg143 pdf  pg155 papel

palavra = {'Laço': 'Repetir uma função várias vezes', 
		'Lista': 'Vários itens entre colchetes',
		'Condicional': 'Executar uma função baseado em falso ou verdadeiro',
		'Variável': 'Item que armazena dados',
		'Indentação': 'Forçar a escrever um código alinhado'}
  
for nome, glossario in palavra.items():
  print(nome.title() + " significa: " + glossario.title() + ".")

