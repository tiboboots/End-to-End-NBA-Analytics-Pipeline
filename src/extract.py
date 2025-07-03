import logging
import nba_api.stats.endpoints as ep
import pandas as pd

logger = logging.getLogger(__name__)

def extract_game_logs(seasons: list, player_or_team_abbreviation: str, 
                      season_type_all_star: str) -> pd.DataFrame:
    dataframes = []
    for season in seasons:
        try:
            season_player_games = ep.LeagueGameLog(season=season, 
            player_or_team_abbreviation=player_or_team_abbreviation,
            season_type_all_star=season_type_all_star).get_normalized_dict()["LeagueGameLog"]

            df = pd.DataFrame(data=season_player_games)
            dataframes.append(df)

        except Exception as e:
            logger.exception(f"Error trying to extract and convert game logs to dataframes: {e}")
            raise

    return pd.concat(objs=dataframes, ignore_index=True)

def extract_team_roster(seasons: list, team_id: int) -> pd.DataFrame:
    dataframes = []
    try:
        for season in seasons:
            season_team_roster = ep.CommonTeamRoster(team_id=team_id, 
            season=season).get_normalized_dict()["CommonTeamRoster"]
            
            df = pd.DataFrame(data=season_team_roster)
            dataframes.append(df)

    except Exception as e:
        logging.exception(f"Error occured trying to extract and convert team roster to dataframe: {e}")
        raise
    
    return pd.concat(objs=dataframes, ignore_index=True)