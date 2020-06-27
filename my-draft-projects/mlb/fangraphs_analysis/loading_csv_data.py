import csv
from pathlib import Path


def get_directories_or_files():
    p = Path('learningpy/mlbprojects/resources/fangraphs_csv')
    data_files = list(p.glob('**/*.csv'))
    return data_files


def load_fangraphs_leaderboard_players_csv_data():
    data_files = get_directories_or_files()
    with data_files[0].open() as csvfile:
        text = csv.reader(csvfile)
        data = []
        for row in text:
            data.append(row)
        return data


def load_fangraphs_leaderboard_teams_csv_data():
    data_files = get_directories_or_files()
    with data_files[1].open() as csvfile:
        text = csv.reader(csvfile)
        data = []
        for row in text:
            data.append(row)
        return data


def list_players():
    data_files = get_directories_or_files()
    with data_files[0].open() as csvfile:
        text = csv.reader(csvfile)
        data_raw = {}
        saltar_primera = True
        for row in text:
            if saltar_primera:
                saltar_primera = False
            else:
                data_raw[row[-1]] = (row[0], row[1])
        return data_raw


def list_teams():
    data_files = get_directories_or_files()
    with data_files[1].open() as csvfile:
        text = csv.reader(csvfile)
        data_raw = {}
        i = 0
        saltar_primero = True
        for row in text:
            if saltar_primero:
                saltar_primero = False
            else:
                data_raw[i] = row[0]
            i+=1
        return data_raw


def get_data_players_cleaned():
    """ Obteniendo los datos solamente, sin los nombres de los jugadores, ni los nombre de
    los equipos ni las abreviaturas de las estadisticas """

    data_files = get_directories_or_files()
    with data_files[0].open() as csvfile:
        text = csv.reader(csvfile)
        data_raw = []
        for row in text:
            data_raw.append(row[2:len(row)])
        data = data_raw[1:]
        
        data_numeric = {}
        
        for d in data:
            data_numeric_fila = []
            for i in range(len(d)-1):
                if d[i].find('.') != -1 and d[i].find('%') != -1:
                    aux = d[i]
                    data_numeric_fila.append(float(aux[:-2]))
                elif d[i].find('.') != -1 and d[i].find('%') == -1:
                    aux = d[i]
                    data_numeric_fila.append(float(aux))
                else:
                    aux = d[i]
                    data_numeric_fila.append(int(aux))
            data_numeric[d[-1]] = data_numeric_fila

        return data_numeric


def get_data_teams_cleaned():
    """ Obteniendo los datos solamente, sin los nombres de los equipos, 
    ni las abreviaturas de las estadisticas """

    data_files = get_directories_or_files()
    with data_files[1].open() as csvfile:
        text = csv.reader(csvfile)
        data_raw = []
        for row in text:
            data_raw.append(row[1:])
        data = data_raw[1:]
        
        data_numeric = {}
        j = 1
        
        for d in data:
            data_numeric_fila = []
            for i in range(len(d)):
                if d[i].find('.') != -1 and d[i].find('%') != -1:
                    aux = d[i]
                    data_numeric_fila.append(float(aux[:-2]))
                elif d[i].find('.') != -1 and d[i].find('%') == -1:
                    aux = d[i]
                    data_numeric_fila.append(float(aux))
                else:
                    aux = d[i]
                    data_numeric_fila.append(int(aux))
            data_numeric[j] = data_numeric_fila
            j+=1

        return data_numeric


def get_statistics_names():
    data_files = get_directories_or_files()
    with data_files[0].open() as csvfile:
        text = csv.reader(csvfile)
        i = 0
        data_raw = []
        data = {}
        for row in text:
            data_raw = row
            break
        for r in data_raw[2:-2]:
            data[i] = r
            i+=1
        return data


""" TODO: Estoy haciendo un mal uso de los diccionario. Tengo un diccionario diferente para cada jugador.
realmente la mejor idea, y la correcta es tener un diccionario donde cada llave contenga una lista con las
estadisticas de cada jugador. (FIXED)"""
