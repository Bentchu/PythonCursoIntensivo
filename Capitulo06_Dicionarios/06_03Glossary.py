#"""6.3 – Glossário: Um dicionário Python pode ser usado para modelar um
#dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
#glossário.
#• Pense em cinco palavras relacionadas à programação que você conheceu
#nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
#armazene seus significados como valores.
#• Mostre cada palavra e seu significado em uma saída formatada de modo
#elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
#significado, ou apresentar a palavra em uma linha e então exibir seu
#significado indentado em uma segunda linha. Utilize o caractere de quebra
#de linha (\n) para inserir uma linha em branco entre cada par palavrasignificado
#em sua saída.
#18/05/21"""

palavra = {'Laço': 'Repetir uma função várias vezes.', 
    'Lista': 'Vários itens entre colchetes.',
    'Condicional': 'Executar uma função baseado em falso ou verdadeiro.',
    'Variável': 'Item que armazena dados.',
    'Indentação': 'Forçar a escrever um código alinhado.'}
    
print("Laço significa: " + palavra['Laço'])
print("Lista significa: " + palavra['Lista'])
print("Condicional significa: " + palavra['Condicional'])
print("Variável significa: " + palavra['Variável'])
print("Indentação significa: " + palavra['Indentação'])
