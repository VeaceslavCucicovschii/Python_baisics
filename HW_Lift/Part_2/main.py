from os import system
from time import sleep

dir_up             = -1
dir_stopped        = 0
dir_down           = 1

building_roof      = True
building_flores    = 9
building_parking   = True

lift_floor         = 3
lift_open          = False
lift_dir           = dir_stopped
lift_target_floor  = 7

human_floor        = 6
human_in_lift      = True  

system('cls')

if building_roof and building_parking:
  start_for = building_flores + 1
  end_for = -1
elif building_roof and not building_parking:
  start_for = building_flores + 1
  end_for = 0
elif building_parking and not building_roof:
  start_for = building_flores
  end_for = -1
else:
  start_for = building_flores
  end_for = 0

while True:

  human_floor = int(input('Where is the human ? '))
  human_in_lift = input('is human inside the lift (y/n) ? ') == 'y'
  call_lift = input('Call the lift (y/n) ? ') == 'y'

  if call_lift:
    if not human_in_lift:
      lift_target_floor = human_floor
    else:
      lift_target_floor = int(input('Where to ? '))

  if lift_floor < lift_target_floor:
    speed = 1
    lift_dir = dir_up
  elif lift_floor > lift_target_floor:
    speed = -1
    lift_dir = dir_down
  else:
    speed = 0

  #################### ANIMATION ####################

  while True:

    lift_floor += speed

    if lift_floor == lift_target_floor:
      lift_open = True
      lift_dir = dir_stopped
      if human_in_lift:
        human_in_lift = False
        human_floor = lift_floor
      else:
        human_in_lift = True

    #################### RENDER FRAME ####################

    system('cls')

    for floor in range(start_for, end_for, -1):

      a = '     '
      c = '     '
      t = '     '
      s = ''

      if floor == start_for:
        t = '-----'

      if floor == lift_floor + 1:
        if lift_dir == dir_down:
          a = '  v  '
        elif lift_dir == dir_up:
          a = '  ^  '
        elif lift_dir == dir_stopped and lift_open:
          a = ' < > '
      elif floor == lift_floor:
        a = '|   |'
        t = '|---|'
        if human_in_lift:
          a = '| H |'
      elif floor == lift_floor - 1:
        t = '|---|'
      if floor == human_floor:
        if not human_in_lift:
          s = ' H'

      print(f'---|{t}|---')
      
      if building_roof and building_parking:
        if floor == start_for:
          print(f' R |{a}|{s}')
        elif floor == end_for + 1:
          print(f' P |{a}|{s}')
        else:
          print(f'{floor:^3}|{a}|{s}')
      elif building_roof and not building_parking:
        if floor == start_for:
          print(f' R |{a}|{s}')
        else:
          print(f'{floor:^3}|{a}|{s}')
      elif building_parking and not building_roof:
        if floor == end_for + 1:
          print(f' P |{a}|{s}')
        else:
          print(f'{floor:^3}|{a}|{s}')
      else:
        print(f'{floor:^3}|{a}|{s}')
    
    if lift_floor == end_for + 1:
      print(        '---||---||---')
    else:
      print(        '---|-----|---')

    #################### RENDER FRAME ####################

    sleep(.7)
    if lift_floor == lift_target_floor:
      break
  #################### ANIMATION ####################