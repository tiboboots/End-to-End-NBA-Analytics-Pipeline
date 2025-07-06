import pandas as pd

def transform_shot_locations(shot_locations: dict):
    columns_and_rows = {}

    result_columns = shot_locations['resultSets']['headers']

    columns = []
    for dict in result_columns:
        columns.extend(dict['columnNames'])

    columns_and_rows['columns'] = columns
    columns_and_rows['rows'] = shot_locations['resultSets']['rowSet']

    return columns_and_rows