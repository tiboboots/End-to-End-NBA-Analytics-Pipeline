import logging
import nba_api.stats.endpoints as ep
import pandas as pd

logger = logging.getLogger(__name__)

def extract_player_games(seasons: list) -> pd.DataFrame:
    dataframes = []
    for season in seasons:
        try:
            season_player_games = ep.LeagueGameLog(season=season, 
                                            player_or_team_abbreviation="P").get_normalized_dict()["LeagueGameLog"]
            df_player_games = pd.DataFrame(data=season_player_games)
            dataframes.append(df_player_games)
        except Exception as e:
            logger.exception(f"Error trying to extract and convert game logs to dataframes: {e}")
            raise
    return pd.concat(objs=dataframes, ignore_index=True)

def extract_team_games(seasons: list) -> pd.DataFrame:
    dataframes = []
    try:
        for season in seasons:
            season_team_games = ep.LeagueGameLog(season=season, 
                                        player_or_team_abbreviation="T").get_normalized_dict()["LeagueGameLog"]
            df_team_games = pd.DataFrame(data=season_team_games)
            dataframes.append(df_team_games)
    except Exception as e:
        logging.exception(f"Error trying to extract and convert team game logs to dataframes: {e}")
        raise
    return pd.concat(objs=dataframes, ignore_index=True)