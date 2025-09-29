#Advent of Code 2022 Day 16
import re
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
    if flow > 0:
        map[valve] = (flow, (simplify_graph(valve, valves)))
    else:
        map.pop(valve)