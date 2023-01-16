#Advent of Code 2022: Day 15 part 2
import re

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def parse_data(lines):
    sensors = {} #sensor: beacon coords
    distances = {} # sensor: manh distance to nearest beacon
    for line in lines:
        sX, sY, bX, bY = list(map(int, reg_num.findall(line)))
        sensors[(sX, sY)] = (bX, bY)
        distances[(sX,sY)] = manh_distance((sX,sY),(bX,bY))
    return sensors, distances

def generator_squared_circle(sensor, radius):
    start_x, start_y = sensor
    directions = [(1,1), (-1,1), (-1,-1), (1,-1)] #downright, downleft, upleft, upright
    coord =  tuple_sum(sensor, (0, -radius)) #move to top corner of sensor reach
    direction = 0
    while direction < 4:
        coord = tuple_sum(coord, directions[direction])
        if start_x == coord[0] or start_y == coord[1]: #at corner make turn
            direction += 1
        yield coord

def in_reach_of_sensor(coord):
    for sens, beac in sensors.items():
        distance_to_coord = manh_distance(coord, sens)
        if distance_to_beacon[sens] >= distance_to_coord:
            return True
    return False

def find_distress_beacon(max_range = 4000000):
    counter = 0
    for sensor, beacon in sensors.items():
        radius = manh_distance(sensor, beacon)
        print("Checking sensor {0}:".format(sensor))
        for coord in generator_squared_circle(sensor, radius + 1): #outer border of sensor reach
            counter += 1
            if counter % 200000 == 0:
                print("  Checked {0} coordinates".format(counter))
            x, y = coord
            if x in range(0, max_range + 1) and y in range(0, max_range + 1):
                if not in_reach_of_sensor(coord):
                    x_res, y_res = coord
                    return x_res * 4000000 + y_res

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
reg_num = re.compile(r"-?\d+")

sensors, distance_to_beacon = parse_data(lines)
print("Task 2:",find_distress_beacon())