from __future__ import print_function
import mlbgame

month = mlbgame.games(2019, 7, home='Braves')
games = mlbgame.combine_games(month)

for game in games:
    print(game)

