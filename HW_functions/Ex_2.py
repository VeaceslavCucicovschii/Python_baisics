from os import system
system('cls')

def inputInt(message):
  print(message, end='')
  n = int(input())
  return n

def inputFloat(message):
  print(message, end='')
  n = float(input())
  return n

def inputBoolean(message, end=''):
  print(message)
  n = bool(input())
  return n

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print( n + m )