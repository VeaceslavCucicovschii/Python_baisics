from os import system
system('cls')

def drawLine(lengh, direction):
  for i in range(lengh):
    if direction == 'h':
      print('-', end='')
    elif direction == 'v':
      print('|')

drawLine( 5, 'h' )