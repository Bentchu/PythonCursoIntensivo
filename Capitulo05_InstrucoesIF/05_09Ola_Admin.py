#5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
#que a lista de usuários não esteja vazia.
#• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
#usuários!
#• Remova todos os nomes de usuário de sua lista e certifique-se de que a
#mensagem correta seja exibida.

#ainda não tá pronto!


usuarios = [ 'josé', 'lucas', 'admin']
usuario = 'Admin'

if usuarios:

	if usuario == 'Admin':
		print("Olá, Admin! Gostaria de ver log?")
	
	elif usuario in usuarios:
		print("Olá, " + usuario + "!")
	
	else:
		print("Usuário não encontrado!")

else:
	print ("Precisamos de algum pangaré!")
