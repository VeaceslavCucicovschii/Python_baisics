from os import system

dir_up           = -1
dir_stopped      = 0
dir_down         = 1

building_roof    = False
building_flores  = 9
building_parking = False

lift_floor       = 3
lift_open        = False
lift_dir         = dir_stopped

human_floor      = 3
human_in_lift    = True

#################### RENDER FRAME ####################

system('cls')

if building_roof:
  print(        '---|-----|----')
  print(        ' R |     |    ')

n = True

for floor in range(building_flores, 0, -1):

  if floor == lift_floor:
    b = '|---|'
  elif floor == lift_floor - 1:
    b = '|---|'
  else:
    b = '     '

  if not building_roof and n:
    print(f'---|-----|----')
    n = False
  else:
    print(f'---|{b}|----')

  if floor == human_floor and not human_in_lift:
    h = ' H  '
  else:
    h = '    '

  if floor == lift_floor + 1 and not human_in_lift:
    l = ' < > '
  elif floor == lift_floor + 1 and human_in_lift:
    l = ' < > '
  else:
    l = '     '

  if floor == lift_floor and not human_in_lift:
    l = '|   |'
  elif floor == lift_floor and human_in_lift:
    l = '| H |'

  print(f'{floor:^3}|{l}|{h}')

if building_parking:
  print(        '---|     |----')
  print(        ' P |     |    ')
  print(        '---|-----|----')
else:
  print(        '---|-----|----')

#################### RENDER FRAME ####################