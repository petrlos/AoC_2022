#Advent of Code 2022: Day 15
import re

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def parse_data(lines):
    sensors = {}
    for line in lines:
        sX, sY, bX, bY = list(map(int, regNum.findall(line)))
        sensors[(sX, sY)] = (bX, bY)
    return sensors

def get_points_on_ref_line(sensor, beacon, ref_line=2000000):
    interval = set()
    sensor_beacon_distance = manh_distance(sensor, beacon)
    sx, sy = sensor
    ref_line_distance = abs(sy-ref_line)
    if sensor_beacon_distance >= ref_line_distance: #reference line lies in area covered by sensor
        delta_x = abs(sensor_beacon_distance - ref_line_distance)
        interval = set(range(sx-delta_x, sx+delta_x+1))
    return interval

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

regNum = re.compile(r"-?\d+")

sensors = parse_data(lines)

result = set()
for sensor, beacon in sensors.items():
    result = result.union(get_points_on_ref_line(sensor, beacon))
for beacon in sensors.values(): #values are coords of beacons
    bx, by = beacon
    if by == 2000000:
        result.discard(bx) #remove beacons, that lies within signal on reference line

print("Task 1:",len(result))