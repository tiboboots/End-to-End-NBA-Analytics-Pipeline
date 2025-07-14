import shot_location_helpers as slh
import logging
from decorators import log
import pandas as pd

logger = logging.getLogger(__name__)


def transform_shot_locations(shot_locations: dict):
    df = slh.shotlocations_to_df(shot_locations=shot_locations)

    metadata_columns, df_flat = slh.shotlocations_combine_columns(shot_locations=shot_locations, df=df)

    shot_locations_df = slh.shotlocations_pivot_df(metadata_columns=metadata_columns, df_flat=df_flat)

    return shot_locations_df


@log
def transform_game_logs(game_logs: dict):
    columns = game_logs['resultSets'][0]['headers']
    rows = game_logs['resultSets'][0]['rowSet']

    game_logs_df = pd.DataFrame(data=rows, columns=columns)

    cols_drop = game_logs_df.columns[(game_logs_df.columns.str.contains("PCT|FANTASY|VIDEO|GAME_ID"))
                                     |(game_logs_df.columns == "REB")]
    game_logs_df = game_logs_df.drop(cols_drop, axis=1)

    return game_logs_df


@log
def transform_lineups(lineups: dict) -> pd.DataFrame:
    columns = lineups['resultSets'][0]['headers']
    rows = lineups['resultSets'][0]['rowSet']

    lineups_df = pd.DataFrame(data=rows, columns=columns)

    cols_drop = lineups_df.columns[(lineups_df.columns.str.contains("PCT|RANK"))
                                   |(lineups_df.columns.isin(["GROUP_SET", "GROUP_ID", "REB"]))]
    lineups_df = lineups_df.drop(cols_drop, axis=1)

    float_cols = lineups_df.select_dtypes(include='float64').columns
    lineups_df[float_cols] = lineups_df[float_cols].astype(int)

    lineups_df = lineups_df.rename(columns={"GROUP_NAME": "LINEUP", "TEAM_ABBREVIATION": "TEAM_SHORT",
                                            "GP": "GAMES", "MIN": "MINUTES"})

    return lineups_df

@log
def transform_hustle_stats(hustle: dict):
    columns = hustle['resultSets'][0]['headers']
    rows = hustle['resultSets'][0]['rowSet']

    hustle_df = pd.DataFrame(data=rows, columns=columns)

    cols_drop = hustle_df.columns[(hustle_df.columns.str.contains("PCT|OFF|DEF|REBS|PTS"))
                                  |(hustle_df.columns == "CONTESTED_SHOTS")]
    hustle_df = hustle_df.drop(cols_drop, axis=1) 

    float_cols = hustle_df.select_dtypes(include='float64').columns
    hustle_df[float_cols] = hustle_df[float_cols].astype(int)

    hustle_df = hustle_df.rename(columns={"G": "GP", "MIN": "MP","TEAM_ABBREVIATION": "TEAM_SHORT"})

    return hustle_df

@log
def transform_player_clutch(clutch: tuple):
    clutch_period, clutch_dict = clutch

    columns = clutch_dict['resultSets'][0]['headers']
    rows = clutch_dict['resultSets'][0]['rowSet']

    clutch_df = pd.DataFrame(data=rows, columns=columns)

    cols_drop = clutch_df.columns[(clutch_df.columns.str.contains("RANK|PCT|FANTASY")) 
                                  |(clutch_df.columns.isin(["DD2", "TD3", "BLKA", "GROUP_SET", "REB", "NICKNAME"]))]
    
    floats_cols = clutch_df.select_dtypes(include='float64').columns
    clutch_df[floats_cols] = clutch_df[floats_cols].astype(int)
    
    clutch_df = clutch_df.drop(cols_drop, axis=1)

    clutch_df = clutch_df.rename(columns={"TEAM_ABBREVIATION": "TEAM_SHORT", "MIN": "MINUTES", "GP": "GAMES"})

    clutch_df.insert(9, 'CLUTCH_PERIOD', clutch_period)

    return clutch_df