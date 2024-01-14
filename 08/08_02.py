
with open("input.txt") as f:
    input = f.readlines()

movements = input[0].strip()
map_list = input[2:]

map_dict = dict()
for line in map_list:
    elements = line.split("=")
    start_node = elements[0].strip()
    end_nodes = elements[1].split(", ")
    end_left_node = end_nodes[0].strip().replace("(", "")
    end_right_node = end_nodes[1].strip().replace(")", "")
    map_dict[start_node] = {"L": end_left_node, "R": end_right_node}

current_nodes = list()
node_iterations = list()
for node in map_dict.keys():
    if node.endswith("A"):
        current_nodes.append(node)
        node_iterations.append(-1)


# BRUTE FORCE -> DOESNT WORK
"""
current_movement_index = 0
res = 0
while True:
    if all([node.endswith("Z") for node in current_nodes]):
        break
    if current_movement_index == len(movements):
        current_movement_index = 0
    current_movement = movements[current_movement_index]
    for index, node in enumerate(current_nodes):
        current_nodes[index] = map_dict[node][current_movement]
    res += 1
    current_movement_index += 1
"""

current_movement_index = 0
res = 0
while True:

    nodes_with_iteration = 0
    for index, node in enumerate(current_nodes):
        if node_iterations[index] == -1 and node.endswith("Z"):
            node_iterations[index] = res
            nodes_with_iteration += 1
        elif node_iterations[index] != -1:
            nodes_with_iteration += 1

    if nodes_with_iteration == len(current_nodes):
        break

    if current_movement_index == len(movements):
        current_movement_index = 0
    current_movement = movements[current_movement_index]
    for index, node in enumerate(current_nodes):
        current_nodes[index] = map_dict[node][current_movement]
    res += 1
    current_movement_index += 1

from math import gcd

lcm = 1
for i in node_iterations:
    lcm = lcm*i//gcd(lcm, i)

print(lcm)
