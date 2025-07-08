import helper_functions_transform as hp
import logging

logger = logging.getLogger(__name__)

def transform_shot_locations(shot_locations: dict):
    try:
        logger.info(f"Extracting shot location header list and converting to exploded dataframe")
        df = hp.shotzones_df(shot_locations=shot_locations)

        logger.info(f"Converting shot locations to a flat dataframe")
        player_data_columns, df_flat = hp.shotzones_flat_df(shot_locations=shot_locations, df=df)

        logger.info(f"Pivoting flat shot locations dataframe to wide version")
        shot_locations_df = hp.shotzones_pivot_df(player_data_columns=player_data_columns, df_flat=df_flat)

        return shot_locations_df
    
    except Exception as e:
        logger.exception(f"Error trying to extract and convert shot locations to wide dataframe: {e}")
        raise