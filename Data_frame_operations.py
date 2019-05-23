import pandas as pd
from Visualize import *
def read_file(filename):
    # Validation code must be written here using the functions available at Visualize class
    dataFrame = Visualize(filename).get_data_file();
    return dataFrame

def get_columns(dataFrame):
    columns = [col for col in dataframe.columns]
    print(columns)
    return columns, len(columns)

def get_columns_type():
    column_types = {}
    for data_type,column_name in dataframe.infer_objects().dtypes.items():
        column_types[data_type] = column_name
    rev_col_type = {}
    for data_type, column_name in sorted(column_types.items()):
        rev_col_type.setdefault(column_name, []).append(data_type)
    return rev_col_type

def get_categorical_variables(dataframe):
    categorical_variables = []
    cols, numa = getColumns(dataframe)
    for col in cols:
        if len(dataframe[col].value_counts()) <=15:
            categorical_variables.append(col)
    return categorical_variables


def get_numerical_variables(dataframe):
    s = getColumnTypes(dataframe)
    cols = []
    for k,v in s.items():
        if k == 'float64' or k == 'int64':
            cols.extend(v)    
    categorical_columns = getCategoricalVariables(dataframe)
    numeric_columns = [x for x in cols if x not in categorical_columns]
    return numeric_columns


def get_cross_tab(dataframe, cat_col_1, cat_col_2):
    data_frame = pd.DataFrame()
    cat_cols = getCategoricalVariables(dataframe)
    if cat_col_1 not in cat_cols or cat_col_2 not in cat_cols:
        return data_frame
    data_frame = pd.crosstab(dataframe[cat_col_1], dataframe[cat_col_2])
    return data_frame


def get_data_frame_info(dataframe, info_cols):
    info = dataframe.describe()
    return info[info_cols]
