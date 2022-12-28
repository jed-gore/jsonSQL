# includes
import numpy as np
import pandas as pd

from os.path import exists

import datetime as dt

from sqlalchemy import create_engine, text
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

# helper functions
def generator():
    n = 1
    while True:
        yield n
        n += 1


class SnowflakeDBConnection:
    def __enter__(self):
        _database = DATABASE
        _schema = SCHEMA
        _account = ""
        _password = ""
        _user = ""
        _wh = ""

        engine = create_engine(
            URL(
                account=_account,
                user=_user,
                password=_password,
                database=_database,
                schema=_schema,
                warehouse=_wh,
            )
        )

        connection = engine.connect()
        self.connection = connection
        self.engine = engine
        return self.connection

    def __exit__(self, type, value, traceback):
        self.connection.close()
        self.engine.dispose()

    def GetConnection(self):
        return self.connection

    def GetEngine(self):
        return self.engine

    def CloseConnection(self):
        self.connection.close()
        self.engine.dispose()


# sql class
class SQL:
    def __init__(self):
        self.conn = SnowflakeDBConnection()

    def execute(self, sql=""):
        results = self.conn.execute(sql).fetchone()
        print(results[0])

    def get_dataframe(self, query=""):
        with self.conn as conn:
            df_result = pd.read_sql(query, conn)
        return df_result


# helper classes
class Table:
    def __init__(self, table_name="", debug=0):
        self.table_name = table_name
        self.dataframe = pd.DataFrame()
        self.debug = debug

    def get_next_id(self, table_name=""):
        tb = Table()
        tb.table_name = table_name
        sql_string = f"select max(id) as id from {table_name}"
        df = self.get_table_data(sql_string)
        id = df.iloc[0]["id"]
        if id is None:
            id = 0
        id = id + 1
        return id

    def get_table_data(
        self,
        sql_string="",
        id="",
        column="",
        column_value="",
        column_values=[],
        debug=0,
    ):
        if sql_string == "":
            sql_string = f"select * from {DATABASE}.{SCHEMA}.{self.table_name}"
        if id != "":
            sql_string = sql_string + " where id = {id}"
        if column != "":
            if column_value != "":
                sql_string = sql_string + f" where {column}='{column_value}'"
            if len(column_values) > 0:
                list_string = "("
                for item in column_values:
                    item = "'" + str(item) + "'"
                    list_string = list_string + item + ","

                list_string = list_string.rstrip(",")
                list_string = list_string + ")"
                sql_string = sql_string + f" where {column} like any {list_string}"
        if debug == 1:
            print(sql_string)
        df = SQL.get_dataframe(sql_string)
        if debug == 1:
            print(df)
        return df

    def truncate_table(self):
        return

    def save(self):
        self.update_table(self.dataframe)

    def update_table(self, df, if_exists="append"):
        with SnowflakeDBConnection() as conn:
            df.to_sql(
                self.table_name,
                con=conn,
                schema=SCHEMA,
                if_exists=if_exists,
                index=False,
                chunksize=16000,
            )
        return
