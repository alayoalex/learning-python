import csv

with open('resources/FanGraphs Leaderboard Players at Bat.csv', newline='') as csvfile:
    text = csv.reader(csvfile)
    i = 0
    index = 0
    statistics = []

    for row in text:
        if i == 0:
            statistics = row
            i+=1
        elif row[0] == 'Giancarlo Stanton':
            for r in range(22):
                print(statistics[index] + ':' + row[index])
                index += 1