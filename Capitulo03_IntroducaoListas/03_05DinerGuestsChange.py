"""3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista."""
#pg80

guests=['Luis Felipe Pondé', 'Carson wentz', 'Pastor Rodolfo', 'Esposa']
message = "Gostaria de jantar comigo, " + guests[0].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[1].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[2].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[3].title() + "?"
print(message)
print(guests[1].title() + ' não poderá comparecer!')
#se usar "remove()", a posição da lista é deletada!
guests[2]='João Paulo Libélula'
message = "Gostaria de jantar comigo, " + guests[0].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[1].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[2].title() + "?"
print(message)
message = "Gostaria de jantar comigo, " + guests[3].title() + "?"
print(message)
