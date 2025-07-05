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
    
    shot_zones = []
    metadata = []

    for tup in df.columns: 
        if len(tup[0]) > 0:
            shot_location = "_".join(tup)
            shot_zones.append(shot_location) 
        else:
            metadata.append(tup[1])

    df.columns = metadata + shot_zones 

    df_long = pd.melt(frame=df, id_vars=metadata, var_name="shot_location", value_name="value") 

    df_long = df_long[df_long['shot_location'].str.contains("FGA") | df_long["shot_location"].str.contains("FGM")]

    df_long[['shot_location', "shot_type"]] = df_long['shot_location'].str.split("_", n=1, expand=True)

    df_wide = df_long.pivot(index = metadata + ['shot_location'], 
                            columns='shot_type', 
                            values='value').reset_index()

    df_wide.columns.name = None

    return df_wide