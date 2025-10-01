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
    return visited

def find_path(pos, time_left, opened, memo):
    key = (pos, time_left, opened)
    if key in memo: return memo[key] #status already found

    _, neighbours = map[pos]

    if time_left <= 2: return 0 #time runs out
    best = 0

    """unopened = [map[val][0] for val, index in valves_indexes.items() if not (1 << index & opened)]

    minutes = time_left
    theoretical_gain = 0
    for val in sorted(unopened, reverse=True):
        minutes -= 2
        if minutes <= 0:
            break
        theoretical_gain += val * minutes
    if (theoretical_gain  <= global_best["value"]): return 0"""

    for next, distance in neighbours.items():
        flow, _ = map[next]
        if next == pos: continue
        if (1 << valves_indexes[next]) & opened: continue #laready opened

        new_time = time_left - distance - 1 # move and open
        if new_time < 0: continue
        gain = flow * new_time
        new_opened = (1 << valves_indexes[next]) | opened
        total = gain + find_path(next, new_time, new_opened, memo)
        best = max(best, total)
        global_best["value"] = max(global_best["value"], best)
    memo[key] = best
    return best

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

reg_valve = re.compile(r"Valve (\w+) .*rate=(\d+).*valves? (.*)")

map = dict()
valves = dict() #neighbours only
for line in lines:
    valve, flow_rate, neighbours = re.search(reg_valve, line).groups()
    valves[valve] = neighbours.split(", ")
    map[valve] = int(flow_rate)

#map: valve: (flow rate, (distance to other valves)), valves with flow=0 are deleted from map
for valve in valves.keys():
    flow = map[valve]
    map[valve] = (flow, (simplify_graph(valve, valves)))

valves_indexes = {key: i for i, key in enumerate(map.keys())}

memo = dict()
global_best = {"value":0}
print(find_path("AA", 30, 0, memo))
print("Runtime:", (datetime.now() - time_start))