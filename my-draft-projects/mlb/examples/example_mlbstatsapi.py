import statsapi

print('The A\'s won %s games in 2018.' % sum(1 for x in statsapi.schedule(team=133,start_date='01/01/2018',
    end_date='12/31/2018') if x.get('winning_team','')=='Oakland Athletics'))
