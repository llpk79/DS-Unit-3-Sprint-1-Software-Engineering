import pandas as pd


class SeparateDateParts(object):
    """Remove date column and replace with separate year, month and day columns.

    """

    def __init__(self, data: pd.DataFrame, column_to_parse: str) -> None:
        self.df = data
        self.column = column_to_parse

    def parse_dates(self) -> pd.DataFrame:
        # Convert column to datetime format.
        self.df[self.column] = pd.to_datetime(self.df[self.column], infer_datetime_format=True)

        # Create columns for year, month and day.
        self.df['year'] = self.df[self.column].dt.year
        self.df['month'] = self.df[self.column].dt.month
        self.df['day'] = self.df[self.column].dt.day

        # Remove original column.
        self.df = self.df.drop(columns=self.column)

        return self.df
