import pandas as pd

def transform_shot_locations(df: pd.DataFrame):
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