import logging
import nba_api.stats.endpoints as ep
import pandas as pd

logger = logging.getLogger(__name__)

def extract_game_logs(season: str, player_or_team_abbreviation: str, 
                      season_type_all_star: str) -> pd.DataFrame:

    season_player_games = ep.LeagueGameLog(season=season, 
    player_or_team_abbreviation=player_or_team_abbreviation,
    season_type_all_star=season_type_all_star).get_dict()

    return season_player_games

def extract_team_roster(season: str, team_id: int) -> pd.DataFrame:
        
    season_team_roster = ep.CommonTeamRoster(team_id=team_id, 
    season=season).get_dict()
    
    return season_team_roster

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