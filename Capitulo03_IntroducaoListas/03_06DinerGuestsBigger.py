"""3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista."""
#pg81

guests=['José', 'João', 'Pedro', 'Tiago']
message = "Gostaria de jantar comigo, " + guests[0].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[1].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[2].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[3].title() + "?"
print(message)
print(guests[0].title() + ' não poderá comparecer!')
#se usar "remove()", a posição da lista é deletada!
guests[0]='João Paulo Libélula'
message = "Gostaria de jantar comigo, " + guests[0].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[1].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[2].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[3].title() + "?"
print(message)
print('Encontrei uma mesa maior, suas frangas!')
guests.insert(0, 'Mateus')
guests.insert(3, 'Tomé')
guests.append('Simão')
message = "Gostaria de jantar comigo, " + guests[0].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[1].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[2].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[3].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[4].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[5].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[6].title() + "?"
print(message)
