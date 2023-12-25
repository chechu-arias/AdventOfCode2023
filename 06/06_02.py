
with open("input.txt") as f:
    input = f.readlines()

race_time = int(input[0].strip().split(":")[1].strip().replace(" ", ""))
race_distance = int(input[1].strip().split(":")[1].strip().replace(" ", ""))

count = 0
for i in range(race_time+1):
    speed = i
    distance_traveled = speed * (race_time-i)
    if distance_traveled > race_distance:
        count += 1

print(count)
