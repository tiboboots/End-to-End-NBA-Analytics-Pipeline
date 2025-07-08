import helper_functions_transform as hp

def transform_shot_locations(shot_locations: dict):
    df = hp.shotzones_df(shot_locations=shot_locations)
    player_data_columns, df_flat = hp.shotzones_flat_df(shot_locations=shot_locations, df=df)
    shot_locations_df = hp.shotzones_pivot_df(player_data_columns=player_data_columns, df_flat=df_flat)

    return shot_locations_df