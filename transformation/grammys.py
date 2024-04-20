import pandas as pd
import re

def process_data(df):
    """
    This function processes data in the DataFrame by extracting artist information from the 'workers' column
    and populating the 'artist' and 'workers' columns accordingly.

    Parameters:
    - df: DataFrame containing Grammy data.

    Returns:
    - df: DataFrame with processed artist and worker information.
    """
    patterns = [r'composer \((.*?)\)', 
                r'\(.*\)',
                r'songwriters? \((.*?)\)']

    def find_artist(workers):
        for pattern in patterns:
            matches = re.findall(pattern, workers)
            if matches:
                return matches[0] if matches[0] else None
        return None

    condition = df['artist'].isnull() & df['workers'].str.contains('|'.join(patterns))

    df.loc[condition, 'artist'] = df.loc[condition, 'workers'].apply(lambda x: find_artist(x) if isinstance(x, str) else None)
    df.loc[df['artist'].notnull() & df['workers'].isnull(), 'workers'] = df['artist']
    return df


def drop_rows(df):
    """
    This function drops rows from the DataFrame where both 'workers' and 'artist' columns are null.

    Parameters:
    - df: DataFrame containing Grammy data.

    Returns:
    - df: DataFrame with rows dropped where both 'workers' and 'artist' columns are null.
    """
    condition = df['workers'].isnull() & df['artist'].isnull()
    df = df[~condition]
    return df


def clean_artist(df):
    """
    This function cleans the 'artist' column in the DataFrame by removing parentheses and their contents.

    Parameters:
    - df: DataFrame containing Grammy data.

    Returns:
    - df: DataFrame with 'artist' column cleaned.
    """
    df['artist'] = df['artist'].str.replace(r'\((.*?)\)', r'\1', regex=True)
    return df

def replace_true_values(df, columns, replacement) -> None:
    """
    This function replaces True values in specified columns of a DataFrame with a given value.

    Parameters:
    - df: Pandas DataFrame.
    - columns: List of column names in which True values will be replaced.
    - replacement: Value to replace True values with.

    Returns:
    - None
    """
    for col in columns:
        df[col] = df[col].replace(True, replacement)


def rename_column(df):
    """
    This function renames the 'winner' column in the DataFrame to 'nominated'.

    Parameters:
    - df: DataFrame containing Grammy data.

    Returns:
    - df: DataFrame with the 'winner' column renamed to 'nominated'.
    """
    df.rename(columns={'winner': 'nominated'}, inplace=True)
    return df


def drop_columns(df):
    """
    This function drops specified columns from the DataFrame.

    Parameters:
    - df: DataFrame containing data.

    Returns:
    - df: DataFrame with specified columns dropped.
    """
    df = df.drop(['id','img', 'published_at', 'updated_at', 'workers', 'title'], axis=1)
    return df


def reemplazar_none_nan(df, valor_reemplazo):
    """
    This function replaces None values with NaN in integer columns of the DataFramer.

    Parameters:
    - df: DataFrame containing data.
    - replacement_value: Value to replace None values with.

    Returns:
    - df: DataFrame with None values replaced with NaN in integer columns.
    """
    columnas_integer = df.select_dtypes(include=['int']).columns

    df[columnas_integer] = df[columnas_integer].fillna(valor_reemplazo)
    return df


def column_year(df, column_name):
    """
    This function transforms a column containing years into a decade representation.

    Parameters:
    - df: DataFrame containing data.
    - column_name: Name of the column containing years.

    Returns:
    - df: DataFrame with the column containing years transformed into decades.
    """
    df[column_name] = df[column_name].astype(int)
    
    for index, value in df[column_name].items():
        if isinstance(value, int) and value % 10 == 0:
            df.at[index, column_name] = value // 10
    
    return df