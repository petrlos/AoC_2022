#Advent of Code 2022 Day 16
import re
from datetime import datetime
time_start = datetime.now()
from functools import lru_cache

from icecream import ic
from collections import deque

def simplify_graph(valve, valves):
    visited = {valve: 0}
    queue = deque([valve])
    while queue:
        current = queue.popleft()
        for neighbour in valves[current]:
            dist = visited[current] + 1
            if neighbour in visited and visited[neighbour] <= dist: continue
            visited[neighbour] = dist
            queue.append(neighbour)
    return {val: dist for val, dist in visited.items() if valves_flow[val] != 0 and val != valve}

def find_path(pos, time_left, opened):
    if (pos, time_left, opened) in cache:
        return cache[(pos, time_left, opened)] #status already found

    if time_left <= 2: return 0 #time runs out - at time = 2 no need to move - cant open anything else
    best = 0

    for next, distance in valves_distances[pos].items():
        if (1 << valves_indexes[next]) & opened: continue #already opened
        new_time = time_left - distance - 1 # move and open
        if new_time < 0: continue
        total = valves_flow[next] * new_time + find_path(next, new_time, 1 << valves_indexes[next] | opened)
        best = max(best, total)
        #global_best["value"] = max(global_best["value"], best)
    cache[(pos, time_left, opened)] = best
    return best

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

reg_valve = re.compile(r"Valve (\w+) .*rate=(\d+).*valves? (.*)")

valves_flow = dict()
valves_neighbours = dict()
for line in lines:
    valve, flow_rate, neighbours = re.search(reg_valve, line).groups()
    valves_flow[valve] = int(flow_rate)
    valves_neighbours[valve] = neighbours.split(", ")

#valves distances = distance to all valves with non-zero flow
valves_distances = dict()
for valve, flow in valves_flow.items():
    if flow == 0 and valve != "AA": continue
    valves_distances[valve] = simplify_graph(valve, valves_neighbours)

#indexes for bitmask
valves_indexes = {key: i for i, key in enumerate(valves_distances.keys())}

cache = {}
print(find_path("AA", 30, 0))
print("Runtime:", (datetime.now() - time_start))