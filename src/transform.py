import shot_location_helpers as slh
import logging
from decorators import log
import pandas as pd

logger = logging.getLogger(__name__)


def transform_shot_locations(shot_locations: dict):
    df = slh.shotlocations_to_df(shot_locations=shot_locations)

    player_data_columns, df_flat = slh.shotlocations_combine_columns(shot_locations=shot_locations, df=df)

    shot_locations_df = slh.shotlocations_pivot_df(player_data_columns=player_data_columns, df_flat=df_flat)

    return shot_locations_df

@log()
def transform_game_logs(game_logs: dict):
    game_log_columns = game_logs['resultSets'][0]['headers']
    game_log_rows = game_logs['resultSets'][0]['rowSet']

    df = pd.DataFrame(data=game_log_rows, columns=game_log_columns)

    cols_to_drop = [col for col in df.columns if 'PCT' in col or col in ['FANTASY_PTS', 'VIDEO_AVAILABLE']]

    if len(cols_to_drop) > 0:
        df = df.drop(cols_to_drop, axis=1)

    return df