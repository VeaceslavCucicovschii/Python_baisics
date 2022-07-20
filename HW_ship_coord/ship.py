big_ship = int(input("ship coordinates: "))

for x in range(1,11):
  if x == int(big_ship - 1):
    print( "w", end="" )
  elif x == big_ship:
    print( "W", end="" )
  elif x == int(big_ship + 1):
    print( "w", end="" )
  else:
    print( "~", end="" )