'''Exercício 8.3, pg 195 Livro Curso Intensivo de Python de Eric Matthes'''
def make_shirt(tamanho, frase):
	print('Você escolheu uma camiseta tamanho ' + str(tamanho) + ' com a mensagem ' + str(frase)+ ' .')
	
tam_cam = input('Qual tamanho da camiseta(P,M,G,GG)?')
fras_cam = input('Qual frase deseja estampar?')
	
make_shirt(tam_cam, fras_cam)
make_shirt(tamanho = 'GG', frase = 'Salva-vidas')
