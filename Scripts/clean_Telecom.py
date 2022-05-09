import pandas as pd
import numpy as np


class DataCleaner:
    """ 
        Returns a DataCleaner Object with the passed DataFrame Data set as its own DataFrame
        Parameters   
   	"""
    def __init__(self, df: pd.DataFrame) -> None:
        
        self.df = df

	    

    def drop_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        Parameters 
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def separate_date_time_column(self, column: str, col_prefix_name: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns is split to date and time new columns adding a prefix string to both
        Parameters
        
        """
        try:

            self.df[f'{col_prefix_name}_date'] = pd.to_datetime(self.df[column]).dt.date
            self.df[f'{col_prefix_name}_time'] = pd.to_datetime(self.df[column]).dt.time

            return self.df

        except:
            print("Failed separation!!!")

    def change_columns_type(self, cols: list, data_type: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        Parameters
        
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print('Failed in changing type!!!')

        return self.df

    def drop_columns_of_single_vlaues(self, unique_value_counts: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a DataFrame where columns with a single value are removed
        Parameters
   
        """
        drop_single = list(unique_value_counts.loc[unique_value_counts['Unique Value Count'] == 1].index)
        return self.df.drop(drop_single, axis=1, inplace=True)

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame where duplicate rows are removed
        Parameters
        """
        remove = self.df[self.df.duplicated()].index
        return self.df.drop(index=remove, inplace=True)

    def fill_numeric_values(self, missing_columns: list, acceptable_skewness: float = 2.0) -> pd.DataFrame:
        """
        Returns a DataFrame where numeric columns are filled with either mean (for acceptbale skewness 
        range i.e. almost normal distr) and median (for beyond acceptable range) based on their 
        skewness Parameters
        
        """
        df_skew_data = self.df[missing_columns]
        df_skewness = df_skew_data.skew(axis=0, skipna=True)
        for i in df_skewness.index:
            if(df_skewness[i] < acceptable_skewness and df_skewness[i] > (acceptable_skewness * -1)):
                val = self.df[i].mean()
                self.df[i].fillna(val, inplace=True)
            else:
                val= self.df[i].median()
                self.df[i].fillna(val, inplace=True)

        return self.df	
    
    def fill_non_numeric_values(self, missing_columns: list, fwd_fill: bool = True, bwd_fill: bool = False) -> pd.DataFrame:
        """
        Returns a DataFrame where non-numeric columns are filled with forward or backward fill
        Parameters
        
        """
        for i in missing_columns:
            if(fwd_fill == True and bwd_fill == True):
                self.df[i].fillna(method='ffill', inplace=True)
                self.df[i].fillna(method='bfill', inplace=True)

            elif(fwd_fill == True and bwd_fill == False):
                self.df[i].fillna(method='ffill', inplace=True)

            elif(fwd_fill == False and bwd_fill == True):
                self.df[i].fillna(method='bfill', inplace=True)

            else:
                self.df[i].fillna(method='ffill', inplace=True)
                self.df[i].fillna(method='bfill', inplace=True)

        return self.df
    
    def bytes_to_megabytes(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where columns value is changed from bytes to megabytes
        """
        try:
            megabyte = 1*10e+5
            for i in columns:
                self.df[i] = self.df[i] / megabyte
                self.df.rename(
                    columns={i: f'{i[:-7]}(MegaBytes)'}, inplace=True)

        except:
            print('failed to convert to MB')

        return self.df
    


    

