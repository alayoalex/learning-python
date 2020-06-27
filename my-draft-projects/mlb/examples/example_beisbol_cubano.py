from pathlib import Path

with open('E:\\workspace\\workspace_python\\learningpy\\mlbprojects\\resources\\beisbol_cubano.txt') as f:
    data = [l for l in f]
    print(data)

print(type(data[0]))

dividido = str.split(data[9], ' ')

print(dividido)

for i in dividido:
    if i != '':
        print(i)