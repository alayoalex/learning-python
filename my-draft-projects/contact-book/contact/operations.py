def save(*data):
    datafile = open("data/data.txt", 'a')
    datafile.write('\n')
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