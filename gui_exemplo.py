''' Exemplo de criação de janela usando PYSimpleGUI.
Do canal YouTube 'Dev Aprender' vídeo "Como Criar Uma Tela Em Python c/ 
PySimpleGUI[Fácil]" '''

from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
	[sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
	[sg.Text('Senha'), sg.Input(key='senha', size=(20,1), password_char='*')],
	[sg.Checkbox('Salvar o login?')],
	[sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)

#Ler os eventos

while True:
	eventos, valores = janela.read()
	if eventos == sg.WINDOW_CLOSED:
		break
	if eventos == 'Entrar':
		if valores['usuario'] == 'jhonatan' and valores ['senha'] == '123456':
			print('Bemvindo a Dev Aprender')
		
	
	
	
