import pandas as pd

def shotzones_df(shot_locations: dict):
    headers = shot_locations['resultSets']['headers']

    df = pd.DataFrame(data=headers).explode(column="columnNames", ignore_index=True).drop_duplicates()
    return df


def shotzones_flat_df(shot_locations: dict, df: pd.DataFrame):
    rows = shot_locations['resultSets']['rowSet']

    shot_zone_columns = df.loc[df['name'] == 'SHOT_CATEGORY', 'columnNames']

    player_data_columns = df.loc[(~ df['columnNames'].str.contains('FG')) 
                        & (df['name'] != 'SHOT_CATEGORY'), 'columnNames'].to_list()

    field_goal_columns = df.loc[df['columnNames'].str.contains('FG'), 'columnNames']

    fg_shot_zones = [f"{zone}_{fg}" for zone in shot_zone_columns for fg in field_goal_columns]

    df_flat = pd.DataFrame(data=rows, columns=player_data_columns+fg_shot_zones)

    return player_data_columns, df_flat


def shotzones_pivot_df(player_data_columns: list , df_flat:pd.DataFrame):

    df_long = df_flat.melt(id_vars=player_data_columns, var_name="shot_category", value_name="shot_value")

    df_long[['shot_category', 'shot_type']] = df_long['shot_category'].str.split("_", n=1 , expand=True)

    shot_locations_df = df_long.pivot(index=player_data_columns + ['shot_category'],
                            columns='shot_type',
                            values='shot_value').reset_index()
    
    shot_locations_df.columns.name = None

    fga = shot_locations_df['FGA']

    shot_locations_df = shot_locations_df.drop(['FGA', 'FG_PCT'], axis=1)
 
    shot_locations_df['FGA'] = fga

    return shot_locations_df