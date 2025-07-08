import helper_functions_transform as hp
import logging
from decorators import log

logger = logging.getLogger(__name__)

@log
def transform_shot_locations(shot_locations: dict):
    df = hp.shotlocations_to_df(shot_locations=shot_locations)

    player_data_columns, df_flat = hp.shotlocations_combine_columns(shot_locations=shot_locations, df=df)

    shot_locations_df = hp.shotlocations_pivot_df(player_data_columns=player_data_columns, df_flat=df_flat)

    return shot_locations_df