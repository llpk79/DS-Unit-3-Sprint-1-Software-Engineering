import pandas as pd


class DeleteColumn(object):
    """Delete and return given column from dataframe.

    """

    def __init__(self, data: pd.DataFrame, column_to_delete: str):
        self.df = data
        self.column = column_to_delete

    def delete_column(self):
        self.df = self.df.drop(columns=self.column)
        return self.df
