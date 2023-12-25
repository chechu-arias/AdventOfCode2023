
with open("input.txt") as f:
    input = f.readlines()

time_line = input[0].strip().split(":")[1].strip().split()
distance_line = input[1].strip().split(":")[1].strip().split()

res = 1
for race_index in range(len(time_line)):
    race_time = int(time_line[race_index])
    race_distance = int(distance_line[race_index])
    print(race_time, race_distance)
    count = 0
    for i in range(race_time+1):
        speed = i
        distance_traveled = speed * (race_time-i)
        if distance_traveled > race_distance:
            count += 1

    res *= count

print(res)
