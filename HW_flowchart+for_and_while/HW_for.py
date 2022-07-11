PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(0, PARKING_PLACES):
    if place_index == FREE_PLACE - 1:
        print("     ", end="")
    else:
        print("| X |", end="")

print("\n", "#"*PARKING_PLACES*5, sep="")
