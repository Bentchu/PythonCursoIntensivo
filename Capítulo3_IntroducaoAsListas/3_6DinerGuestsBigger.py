guests=['Luiz', 'Massami', 'Rodrigo', 'Andressa']
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
guests.insert(0, 'Paulo')
guests.insert(3, 'Bruno')
guests.append('Vicente')
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
