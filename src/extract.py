import logging
import nba_api.stats.endpoints as ep
import pandas as pd

logger = logging.getLogger(__name__)

def extract_game_logs(seasons: list, player_or_team_abbreviation: str, 
                      season_type_all_star: str) -> pd.DataFrame:
    dataframes = []

    for season in seasons:
        season_player_games = ep.LeagueGameLog(season=season, 
        player_or_team_abbreviation=player_or_team_abbreviation,
        season_type_all_star=season_type_all_star).get_normalized_dict()["LeagueGameLog"]

        df = pd.DataFrame(data=season_player_games)
        dataframes.append(df)

    return pd.concat(objs=dataframes, ignore_index=True)

def extract_team_roster(seasons: list, team_id: int) -> pd.DataFrame:
    dataframes = []

    for season in seasons:
        season_team_roster = ep.CommonTeamRoster(team_id=team_id, 
        season=season).get_normalized_dict()["CommonTeamRoster"]
        
        df = pd.DataFrame(data=season_team_roster)
        dataframes.append(df)
    
    return pd.concat(objs=dataframes, ignore_index=True)

def extract_shot_locations(season: str, player_or_team: str, 
                           season_type_all_star: str = "Regular Season") -> pd.DataFrame:
    
    if player_or_team.lower() == "player":
        df = ep.LeagueDashPlayerShotLocations(season=season, 
        season_type_all_star=season_type_all_star).get_data_frames()[0]
    
    elif player_or_team.lower() == "team":
        df = ep.LeagueDashTeamShotLocations(season=season,
        season_type_all_star=season_type_all_star).get_data_frames()[0]

    else:
        logger.error(f"Incorrect value for player_or_team parameter in extract_shot_locations", exc_info= True)
        raise ValueError

    return df