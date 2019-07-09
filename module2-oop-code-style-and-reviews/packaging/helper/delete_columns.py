import pandas as pd


class DeleteColumn(object):
    """Delete and return given column from DataFrame.

    """

    def __init__(self, data: pd.DataFrame, column_to_delete: str) -> None:
        self.df = data
        self.column = column_to_delete

    def delete_column(self) -> pd.DataFrame:
        self.df = self.df.drop(columns=self.column)
        return self.df
