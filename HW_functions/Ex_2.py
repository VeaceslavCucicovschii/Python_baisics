from os import system
system('cls')

def inputInt(message):
  n = int(input(message))
  return n

def inputFloat(message):
  n = float(input(message))
  return n

def inputBoolean(message):
  n = input(message) == 'True'
  return n

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print( n + m )
