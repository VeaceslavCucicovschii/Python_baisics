clientsHighPriority = ["Tob","Pete"]
clients = ["John", "Marry", "Kate"]
clientsLowPriority = ["Vicky","Lessly"]

counter = 1

for i in range(len(clientsHighPriority)):
  print(f'{counter}. {clientsHighPriority[i]}')
  counter += 1

for i in range(len(clients)):
  print(f'{counter}. {clients[i]}')
  counter += 1

for i in range(len(clientsLowPriority)):
  print(f'{counter}. {clientsLowPriority[i]}')
  counter += 1