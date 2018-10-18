def get_data():
    data = input().strip('\r').split(" ")
    jim_ratt = {}
    # for num in data:
    #
    #     jim_ratt.append(int(num))
    for num in range(1, 10 + 1):  # this could be in the lower loop
        times = []
        times.append(int(data.pop()))
        times.append(int(data.pop()))
        jim_ratt[num] = times
    # print(jim_ratt)

    # print("jim: ", jim_ratt)

    other_machines = {}
    for num in range(1, 10 + 1):
        other_machines[num] = input()
        # print(num, ": ", other_machines[num])

    return jim_ratt, other_machines


def find_time(jim, other_machines):
    current_time = 0
    for iteration in range(1, 4):
        # print("Jim's ", iteration, "th cycle: ")
        current_time += one_cycle(current_time, jim, other_machines)
    return current_time


def one_cycle(current_time, jim, other_machines):
    for current_machine in range(1, 10 + 1):
        current_time += one_machine(current_machine, current_time, jim, other_machines)
    return current_time


def one_machine(current_machine, current_time, jim, other_machines):
    other_usage, other_recovery, other_start = other_machines[current_machine].split(" ")
    if current_time < int(other_start):
        # print("Jim")
        current_time += jim[current_machine][0]  # workout
        current_time += jim[current_machine][1]  # recovery
    else:
        # print("Jim needs to wait")
        current_time + int(other_start) + int(other_usage) + int(other_recovery)
        current_time += jim[current_machine][0]  # workout
        current_time += jim[current_machine][1]  # recovery
        print(current_time)
    return current_time

    # print(other_usage, other_recovery, other_start)


jim, other_machines = get_data()
print(find_time(jim, other_machines))
