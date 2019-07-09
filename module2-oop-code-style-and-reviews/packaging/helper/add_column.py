import pandas as pd


class AddColumn(object):
    """Add a column to a pandas DataFrame using a list.

    Convert list to Series and concatenate to DataFrame on axis 1.

    """

    def __init__(self, data: pd.DataFrame, new_column: list, new_column_name: str) -> None:
        self.df = data
        self.new_column = pd.Series(new_column, name=new_column_name)

    def add_column(self) -> pd.DataFrame:
        # Maintain list order by setting sort=False.
        self.df = pd.concat([self.df, self.new_column], axis=1, sort=False)
        return self.df

