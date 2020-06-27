import loading_csv_data, statistics_meaning


def menu():
    print('------------ MENU ------------')
    print('Seleccione el numero de la opcion de su preferencia:')
    print('0. Salir')
    print('1. Estadisticas Individuales')
    print('2. Estadisticas Colectivas')
    print('3. Nombres de las Estadisticas')


print('\nSYSTEMA DE ANÁLISIS DE ESTADÍSTICAS DE GRANDES LIGAS')
print('Fuente de Datos Principal: FanGraphs Web Sites. www.fangraphs.com')
print('Autor: Alexei Alayo Rondon')

print()

print('------------ MENU ------------')
print('Seleccione el numero de la opcion de su preferencia:')
print('0. Salir')
print('1. Estadisticas Individuales')
print('2. Estadisticas Colectivas')
print('3. Nombres de las Estadisticas')

n = int(input())

players = loading_csv_data.list_players()
teams = loading_csv_data.list_teams()
statistics_names = loading_csv_data.get_statistics_names()
players_statistics = loading_csv_data.get_data_players_cleaned()
teams_statistics = loading_csv_data.get_data_teams_cleaned()

while n != 0:
    if n == 1:        
        print('\nHay ' + str(len(players)) + ' Jugadores en la lista.')
        print('-----------------------------')
        for k,v in players.items():
            print(k + '. ' + v[0] + ' (' + v[1] + ')', end='\n')
        
        # TODO: Organizar la salida de los datos de los jugadores, preferiblemente en una funcion aparte
        id_seleccionado = input('\nSeleccione el jugador introduciendo su ID \n')
        print('\n' + players[id_seleccionado][0])
        for p in range(len(statistics_names)):
            print(statistics_meaning.statistics_feats_english[statistics_names[p]] + ': ' + str(players_statistics[id_seleccionado][p]))
        n = int(input('\nIntroduzca 9 para volver al menú o presione 0 para salir.\n'))
    
    elif n == 2:
        print('\nHay ' + str(len(teams)) + ' Equipos en la lista')
        print('--------------------------')
        for k,v in teams.items():
            print(str(k) + '. ' + v, end='\n')

        id_seleccionado = int(input('\nSeleccione el equipo introduciendo su ID \n'))
        print('\n' + teams[id_seleccionado])
        for p in range(len(statistics_names)):
            print(statistics_meaning.statistics_feats_english[statistics_names[p]] + ': ' + str(teams_statistics[id_seleccionado][p]))
        n = int(input('\nIntroduzca 9 para volver al menú o presione 0 para salir.\n'))
    
    elif n == 3:        
        print('\nHay ' + str(len(statistics_names)) + ' parametros estadisticos en analisis')
        print('-----------------------------------------------')
        for k,v in statistics_names.items():
            print(str(k) + '. ' + v + ' => ' + statistics_meaning.statistics_feats_english[v], end='\n')
        n = int(input('\nIntroduzca 9 para volver al menú o presione 0 para salir.\n'))

    elif n == 9:
        menu()
        n = int(input())
