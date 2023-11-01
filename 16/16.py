#Advent of Code 2022 - Day 16
import re
from collections import deque
from itertools import permutations
from pprint import pprint as pp

def test(): #created on paper for test purpose
    nodes_by_hand = {
        "BB": {"CC": 1, "DD": 2, "EE": 3, "HH": 6, "JJ": 3},
        "CC": {"BB": 1, "DD": 1, "EE": 2, "HH": 5, "JJ": 4},
        "DD": {"BB": 2, "CC": 1, "EE": 1, "HH": 4, "JJ": 3},
        "EE": {"BB": 3, "CC": 2, "DD": 1, "HH": 3, "JJ": 4},
        "HH": {"BB": 6, "CC": 5, "DD": 4, "EE": 3, "JJ": 7},
        "JJ": {"BB": 3, "CC": 4, "DD": 3, "EE": 4, "HH": 7},
    }

def get_distances_to_valves_with_flow(lines):
    def bfs_simplify_graph(start):
        distances = {start: 0}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbour in all_valves[current][1]:
                if neighbour not in distances.keys():
                    distances[neighbour] = distances[current] + 1
                    queue.append(neighbour)
        for key in list(distances.keys()):
            if key not in valves: #remove all valves without flow
                distances.pop(key)
        distances.pop(start, None)
        return distances

    valves, valves_flow, valves_dist, all_valves = {}, {}, {}, {}
    reg_valve = re.compile(r"Valve (\w+) .*rate=(\d+).*valves? (.*)")
    for line in lines:
        valve, flow_rate, neighbours = re.search(reg_valve, line).groups()
        flow_rate = int(flow_rate)
        all_valves[valve] = [flow_rate, neighbours.split(", ")]
        if flow_rate > 0:
            valves[valve] = dict()
    for valve in valves.keys():
        valves_dist[valve] = bfs_simplify_graph(valve)
        valves_flow[valve] = all_valves[valve][0]
    start = bfs_simplify_graph("AA")
    return start,valves_dist,valves_flow

def brute_force_sollution(): #dont use for real data
    def count_pressure(way):
        current = "AA"
        output = 0
        time = 30
        while way:
            distance = valves_dist[current]
            distance = distance[way[0]]
            time -= distance + 1  # traveldistance + time to open
            current, way = way[0], way[1:]
            output += time * valves_flow[current]
        return output

    all_possible_ways = (permutations(valves_dist.keys()))
    valves_dist["AA"] = starter

    outputs = []
    for way in all_possible_ways:
        output = count_pressure(list(way))
        outputs.append(output)
    return max(outputs)

#MAIN

with open("test.txt") as file:
    lines = file.read().splitlines()

starter, valves_dist, valves_flow = get_distances_to_valves_with_flow(lines)

print(brute_force_sollution())