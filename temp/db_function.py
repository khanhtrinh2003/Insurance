
import sqlite3
import pandas as pd
import numpy as np
import datetime

def convert_timestamp(x):
    return datetime.datetime.fromtimestamp(x['TradingDate']).strftime('%Y-%m-%d')

class My_db():
    def __init__(self,database) -> None:
        self.database=database
        
        
    def get_database_table(self):
        
        self.cursor= self.database.cursor()
        # Execute the query to get the table names
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # replace with appropriate query for your database

        # Fetch all the table names
        tables = self.cursor.fetchall()

        # Print the table names
        for table in tables:
            print(table[0])

        # Commit the changes
        self.database.commit()

        # Close the self.cursor and connection
        self.cursor.close()

    def delete_database_table(self,name):
        # Get the self.cursor
        
        self.cursor= self.database.cursor()
        # Execute the query to delete the table
        self.cursor.execute(f"DROP TABLE IF EXISTS {name};") # replace "table_name" with the name of the table you want to delete

        # Commit the changes
        self.database.commit()

        # Close the self.cursor and connection
        self.cursor.close()

    def get_shape_database(self):
        
        self.cursor= self.database.cursor()
        # Get the table names
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()

        # Iterate through the tables and get their shape
        for table in tables:
            table_name = table[0]
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            num_rows = self.cursor.fetchone()[0]
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            num_cols = len(self.cursor.fetchall())
            print(f"{table_name}: {num_rows} rows, {num_cols} columns")

        # Close the self.cursor and connection
        self.cursor.close()   

    def read_data(self, table) -> pd.DataFrame:
        df=pd.read_sql(f"SELECT * FROM {table}", self.database)
        return df.set_index(df.columns[0])
    
     
    def save_database_tabe(self,df,table,mode="append"):
        df.to_sql(f"{table}",con=self.database,if_exists=mode,index=False)  
    
    
    def close_db(self):
        self.cursor.close()  