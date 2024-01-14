
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

current_node = "AAA"
current_movement_index = 0
res = 0
while current_node != "ZZZ":
    if current_movement_index == len(movements):
        current_movement_index = 0
    current_movement = movements[current_movement_index]
    current_node = map_dict[current_node][current_movement]
    res += 1
    current_movement_index += 1

print(res)