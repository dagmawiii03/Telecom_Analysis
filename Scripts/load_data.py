import pandas as pd

missing_values = ["n/a", "na", 'none', "-", "--", None, '?']


def load_df_from_csv(filename: str, na_values: list = []) -> pd.DataFrame:
    """
        A simple function which tries to load a dataframe from a specified .csv filename 
        returning the loaded DataFrame
        
    """
    try:
        na_values.extend(missing_values)
        df = pd.read_csv(filename, na_values=na_values)
        df = optimize_data(df)

        return df
    except:
        print("Error Occured:\n\tCould not find specified .csv file")


def load_df_from_excel(filename: str, na_values: list = []) -> pd.DataFrame:
    """
       A simple function which tries to load a dataframe from a specified .xslx filename 
       returning the loaded DataFrame
       
    """
    try:
        na_values.extend(missing_values)
        df = pd.read_excel(
            filename, na_values=na_values, engine='openpyxl')
        df = optimize_data(df)

        return df
    except:
        print("Error Occured:\n\tCould not find specified .xslx file")


def optimize_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
       A simple function which optimizes the data types of the dataframe and returns it
        
    """
    data_types = dataframe.dtypes
    optimize = ['float64', 'int64']

    for i in data_types.index:
        if(data_types[i] in optimize):
            if(data_types[i] == 'float64'):
                dataframe[i] = pd.to_numeric(
                    dataframe[i], downcast='float')  # downcasting a float column

            elif(data_types[i] == 'int64'):
                dataframe[i] = pd.to_numeric(
                    dataframe[i], downcast='unsigned')  # downcasting an integer column

    return dataframe