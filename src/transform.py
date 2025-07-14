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

@log()
def transform_game_logs(game_logs: dict):
    game_log_columns = game_logs['resultSets'][0]['headers']
    game_log_rows = game_logs['resultSets'][0]['rowSet']

    df = pd.DataFrame(data=game_log_rows, columns=game_log_columns)

    cols_to_drop = [col for col in df.columns if 'PCT' in col 
                    or col in ['FANTASY_PTS', 'VIDEO_AVAILABLE', 'GAME_ID']]

    df = df.drop(cols_to_drop, axis=1)

    return df

@log()
def transform_team_roster(team_roster: dict):
    team_roster_columns = team_roster['resultSets'][0]['headers']
    team_roster_rows = team_roster['resultSets'][0]['rowSet']

    df = pd.DataFrame(data=team_roster_rows, columns=team_roster_columns)

    df = df.drop(['LeagueID', 'PLAYER_SLUG', 'NICKNAME'], axis=1)

    df['BIRTH_DATE'] = pd.to_datetime(df['BIRTH_DATE'], format="%b %d, %Y")

    return df

@log()
def transform_lineups(lineups: dict) -> pd.DataFrame:
    columns = lineups['resultSets'][0]['headers']
    rows = lineups['resultSets'][0]['rowSet']

    lineups_df = pd.DataFrame(data=rows, columns=columns)

    cols_drop = [col for col in lineups_df.columns if 'RANK' in col or 'PCT' in col or col == 'GROUP_SET']
    df = lineups_df.drop(cols_drop, axis=1)

    float_cols = lineups_df.select_dtypes(include='float64').columns
    lineups_df[float_cols] = lineups_df[float_cols].astype(int)

    return lineups_df