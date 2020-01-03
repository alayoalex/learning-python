import os


def counter():
    if not os.path.exists("data/counter.txt"):
        count = open("data/counter.txt", 'w')
        count.write(str(1))
        count.close()
    else:
        count = open("data/counter.txt", 'r')
        c = int(count.read())
        c += 1
        countmore = open("data/counter.txt", 'w')
        countmore.write(str(c))
        return c
        

def save(*data):
    c = counter()
    datafile = open("data/data%s.txt" %(c), 'w')
    for i in range(len(data)):
        datafile.write(data[i] + '\n')


def update(parameter_list):
    pass


def delete(self, parameter_list):
    pass


def listing(parameter_list):
    pass   


def get(parameter_list):
    pass


def sorting(self, parameter_list):
    pass 