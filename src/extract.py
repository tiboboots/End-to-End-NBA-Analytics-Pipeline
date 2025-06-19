from nba_api.stats.static import teams, players

def get_team_ids():
    all_nba_teams = teams.get_teams()
    all_teams = {}

    for team in all_nba_teams:
        team_id = team['id']
        team_name = team['full_name']
        all_teams[team_name] = team_id
    return all_teams

def get_active_player_ids():
    all_nba_players = players.get_players()
    all_active_players = {}

    for player in all_nba_players:
        if player['is_active'] == False:
            continue # Skip all non-active players
        player_id = player['id']
        player_name = player['full_name']
        all_active_players[player_name] = player_id
    return all_active_players