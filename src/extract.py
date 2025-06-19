from nba_api.stats.static import teams, players

def get_team_ids() -> dict:
    all_nba_teams = teams.get_teams()
    all_teams = {}

    for team in all_nba_teams:
        team_id = team['id']
        team_name = team['full_name']
        all_teams[team_name] = team_id
    return all_teams

def get_active_player_ids() -> dict:
    all_active_players = players.get_active_players()
    active_players_ids = {}

    for player in all_active_players:
        player_id = player['id']
        player_name = player['full_name']
        active_players_ids[player_name] = player_id
    return active_players_ids

def get_inactive_player_ids() -> dict:
    all_inactive_players = players.get_inactive_players()
    inactive_players_ids = {}

    for player in all_inactive_players:
        player_name = player["full_name"]
        player_id = player["id"]
        inactive_players_ids[player_name] = player_id
    return inactive_players_ids