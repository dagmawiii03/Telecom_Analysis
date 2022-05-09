import pandas as pd
import numpy as np
import sys
import os


class DataCleaner:
    """ 
        Returns a DataCleaner Object with the passed DataFrame Data set as its own DataFrame
          
   	"""  
    pd.set_option('max_columns', None)
    pd.set_option('max_rows', None)
    df = pd.read_excel('data/challenge_data_source.xlsx')

    def __init__(self, df: pd.DataFrame) -> None:
        
        self.df = df  

    def drop_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def separate_date_time_column(self, column: str, col_prefix_name: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns is split to date and time new columns adding a prefix string to both
        
        
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
        
   
        """
        drop_single = list(unique_value_counts.loc[unique_value_counts['Unique Value Count'] == 1].index)
        return self.df.drop(drop_single, axis=1, inplace=True)

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame where duplicate rows are removed
        
        """
        remove = self.df[self.df.duplicated()].index
        return self.df.drop(index=remove, inplace=True)

    def fill_numeric_values(self, missing_columns: list, acceptable_skewness: float = 2.0) -> pd.DataFrame:
        """
        Returns a DataFrame where numeric columns are filled with either mean (for acceptbale skewness 
        range i.e. almost normal distr) and median (for beyond acceptable range) based on their 
        skewness 
        
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

    def data_outlier(self, columns: list) -> pd.DataFrame:
        
        """
        Returns a DataFrame where outlier of the specified columns is fixed
        Parameters for column list

        """
        try:
            for i in columns:
                self.df[i] = np.where(self.df[i] > self.df[i].quantile(
                    0.95), self.df[i].median(), self.df[i])
        except:
            print("outliers can't be fixed")

        return self.df
    
    def standardized_column(self, columns: list, new_name: list, func) -> pd.DataFrame:
        """
        Returns a DataFrame where specified columns are standardized based on a given function 
        and given new names 
        
        """
        try:
            assert(len(columns) == len(new_name))
            for index, col in enumerate(columns):
                self.df[col] = func(self.df[col])
                self.df.rename(columns={col: new_name[index]}, inplace=True)

        except:
            print('standardization failed!!!')

        return self.df
    
    def optimize_data(self) -> pd.DataFrame:
        """
        Returns the DataFrames information after all column data types are optimized 
        (to minimize in data type without affecting system behaviour in required 
        tolerance)
        """
        data_types = self.df.dtypes
        optimize = ['float64', 'int64']
        
        for i in data_types.index:
            if(data_types[i] in optimize):

                if(data_types[i] == 'float64'):
                     self.df[i] = pd.to_numeric(
                        self.df[i], downcast='float')    # optimizing a float column
                
                elif(data_types[i] == 'int64'):
                    self.df[i] = pd.to_numeric(
                        self.df[i], downcast='unsigned')   # optimizing an integer column

        return self.df.info()


    def save_clean_data(self, name: str):
        """
        collective objective DataFrame gets saved as csv file
        
        """
        try:
            self.df.to_csv(name)

        except:
            print("saving failed!!!") 
    
    
     

    

    
    


    

