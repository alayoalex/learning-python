import csv

with open('resources/FanGraphs Leaderboard Teams at Bat.csv', newline='') as csvfile:
    text = csv.reader(csvfile)
    i = 0
    data = []
    for row in text:
        data.append(row)

    print(data)
    print(type(data[2][1]))

    g = int(data[2][1])

    print(g)
    print(type(g))