import pandas as pd
from decorators import log

@log
def shotlocations_to_df(shot_locations: dict):
    headers = shot_locations['resultSets']['headers']

    df = pd.DataFrame(data=headers).explode(column="columnNames", ignore_index=True).drop_duplicates()
    return df

@log
def shotlocations_combine_columns(shot_locations: dict, df: pd.DataFrame):
    rows = shot_locations['resultSets']['rowSet']

    shot_zone_columns = df.loc[df['name'] == 'SHOT_CATEGORY', 'columnNames']

    metadata_columns = df.loc[(~ df['columnNames'].str.contains('FG')) 
                        & (df['name'] != 'SHOT_CATEGORY'), 'columnNames'].to_list()

    field_goal_columns = df.loc[df['columnNames'].str.contains('FG'), 'columnNames']

    fg_shot_zones = [f"{zone}_{fg}" for zone in shot_zone_columns for fg in field_goal_columns]

    df_flat = pd.DataFrame(data=rows, columns=metadata_columns+fg_shot_zones)

    return metadata_columns, df_flat

@log
def shotlocations_pivot_df(metadata_columns: list , df_flat:pd.DataFrame):

    df_long = df_flat.melt(id_vars=metadata_columns, var_name="shot_location", value_name="shot_value")

    df_long[['shot_location', 'shot_type']] = df_long['shot_location'].str.split("_", n=1 , expand=True)

    shot_locations_df = df_long.pivot(index=metadata_columns + ['shot_location'],
                            columns='shot_type',
                            values='shot_value').reset_index()
    
    shot_locations_df.columns.name = None

    fga = shot_locations_df['FGA']

    if 'NICKNAME' in shot_locations_df.columns:
        shot_locations_df = shot_locations_df.drop(['FGA', 'FG_PCT', 'NICKNAME'], axis=1)
    else:
        shot_locations_df = shot_locations_df.drop(['FGA', 'FG_PCT'], axis=1)
 
    shot_locations_df['FGA'] = fga
    
    if 'AGE' in shot_locations_df.columns:
        shot_locations_df[['FGM', 'FGA', 'AGE']] = shot_locations_df[['FGM', 'FGA', 'AGE']].fillna(0.0).astype(int)
    else:
        shot_locations_df[['FGM', 'FGA']] = shot_locations_df[['FGM', 'FGA']].fillna(0.0).astype(int)

    return shot_locations_df