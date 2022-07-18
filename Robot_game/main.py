from os import system
import random

system("cls")  # linux -> "clear"

def killer_direction_moove(x, y):
  direction = random.randint(1, 4)
  if direction == 1:
    x -= 1;
  elif direction == 2:
    y -= 1;
  elif direction == 3:
    x += 1;
  else:
    y += 1;
  return x, y

def killer_direction_moove_to_robot(x, y, end_x, end_y):
  if x > end_x:
    x -= 1;
  elif y > end_y:
    y -= 1;
  elif x < end_x:
    x += 1;
  elif y < end_y:
    y += 1;
  return x, y

def killer_at_border(x, y):
  if x > 30:
    x -= 1;
  elif y > 12:
    y -= 1;
  elif x < 1:
    x += 1;
  elif y < 1:
    y += 1;
  return x, y

lenght_x = 30
lenght_y = 12

result = False
steps = 0
x = 1
y = 1

robot_coord_x = 15
robot_coord_y = 6

killer_1_coord_x = 15
killer_1_coord_y = 3

killer_2_coord_x = 15
killer_2_coord_y = 9

killer_3_coord_x = 7
killer_3_coord_y = 6

killer_4_coord_x = 23
killer_4_coord_y = 6

while True:
  for y in range(1, lenght_y + 1):
    for x in range(1, lenght_x + 1):

      if x == robot_coord_x and y == robot_coord_y:
        print("R", end="")
      elif x == killer_1_coord_x and y == killer_1_coord_y:
        print("K", end="")
      elif x == killer_2_coord_x and y == killer_2_coord_y:
        print("K", end="")
      elif x == killer_3_coord_x and y == killer_3_coord_y:
        print("K", end="")
      elif x == killer_4_coord_x and y == killer_4_coord_y:
        print("K", end="")
      else:
        print("-", end="")
    print("")

  direction = input("use (w/a/s/d) to move >>> ")

  if direction == "a":
    robot_coord_x -= 1
  elif direction == "w":
    robot_coord_y -= 1
  elif direction == "d":
    robot_coord_x += 1
  elif direction == "s":
    robot_coord_y += 1
  else:
    print("So you chose not to move, OK")

  killer_1_coord_x, killer_1_coord_y = killer_direction_moove_to_robot(killer_1_coord_x, killer_1_coord_y, robot_coord_x, robot_coord_y)
  killer_2_coord_x, killer_2_coord_y = killer_direction_moove_to_robot(killer_2_coord_x, killer_2_coord_y, robot_coord_x, robot_coord_y)
  killer_3_coord_x, killer_3_coord_y = killer_direction_moove(killer_3_coord_x, killer_3_coord_y)
  killer_4_coord_x, killer_4_coord_y = killer_direction_moove(killer_4_coord_x, killer_4_coord_y)

  killer_1_coord_x, killer_1_coord_y = killer_at_border(killer_1_coord_x, killer_1_coord_y)
  killer_2_coord_x, killer_2_coord_y = killer_at_border(killer_2_coord_x, killer_2_coord_y)
  killer_3_coord_x, killer_3_coord_y = killer_at_border(killer_3_coord_x, killer_3_coord_y)
  killer_4_coord_x, killer_4_coord_y = killer_at_border(killer_4_coord_x, killer_4_coord_y)

  steps += 1
  if robot_coord_x > lenght_x or robot_coord_y > lenght_y \
      or robot_coord_x < 1 or robot_coord_y < 1 \
      or robot_coord_x == killer_1_coord_x and robot_coord_y == killer_1_coord_y \
      or robot_coord_x == killer_2_coord_x and robot_coord_y == killer_2_coord_y \
      or robot_coord_x == killer_3_coord_x and robot_coord_y == killer_3_coord_y \
      or robot_coord_x == killer_4_coord_x and robot_coord_y == killer_4_coord_y:
    result = False
    break
  elif steps == 30:
    result = True
    break
  
  system("cls")  # linux -> "clear"

print("")
if result == True:
  print("Your steps = 30, YOU WON")
else:
  print("YOU LOSE\nYour steps =", steps)
print("")
