import shot_location_helpers as slh
import logging
from decorators import log

logger = logging.getLogger(__name__)


def transform_shot_locations(shot_locations: dict):
    df = slh.shotlocations_to_df(shot_locations=shot_locations)

    player_data_columns, df_flat = slh.shotlocations_combine_columns(shot_locations=shot_locations, df=df)

    shot_locations_df = slh.shotlocations_pivot_df(player_data_columns=player_data_columns, df_flat=df_flat)

    return shot_locations_df