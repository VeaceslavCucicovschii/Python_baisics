# plane_homework
plane_altitude = 500    # meters
plane_speed = 300    # km/hours

runways_for_landing = True

wind_speed = 140    # km/hours
wind_direction = 'South_East'
plane_direction = 'South_East'

conbustible = 50    # percent
defects = False

# logic
can_land = plane_altitude < 700 and plane_speed < 500 and plane_altitude <= 100 and plane_speed >= 200 \
    and runways_for_landing == True and wind_speed <= 100 and plane_direction == wind_direction \
    or conbustible == 1 or defects == True

# view
print("Can the plane land ?", can_land)

# robot_homework

# 17 steps
# 2 steps right and 1 step down
# steps_right, steps_left, steps_down, steps_up
