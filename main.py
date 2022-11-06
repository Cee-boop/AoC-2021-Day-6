with open(file='data.txt') as file:
    birthing_schedule = {}
    for num in file.read().split(","):
        if int(num) in birthing_schedule:
            birthing_schedule[int(num)] += 1
        else:
            birthing_schedule[int(num)] = 1


def lanternfish_count_simulation(days):
    global birthing_schedule
    for day in range(days):
        if day in birthing_schedule:

            if day + 7 in birthing_schedule:
                birthing_schedule[day + 7] += birthing_schedule[day]
            else:
                birthing_schedule[day + 7] = birthing_schedule[day]

            if day + 9 in birthing_schedule:
                birthing_schedule[day + 9] += birthing_schedule[day]
            else:
                birthing_schedule[day + 9] = birthing_schedule[day]

            birthing_schedule.pop(day)

    return print(sum(birthing_schedule.values()))


# part one:
lanternfish_count_simulation(80)
# part two:
lanternfish_count_simulation(256)
