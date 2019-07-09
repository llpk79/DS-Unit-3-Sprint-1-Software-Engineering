import pandas as pd


class SeparateDateParts(object):
    """Remove date column and replace with separate year, month and day columns

    """

    def __init__(self, data: pd.DataFrame, column_to_parse: str):
        self.df = data
        self.column = column_to_parse

    def parse_dates(self):
        self.df[self.column] = pd.to_datetime(self.df[self.column], infer_datetime_format=True)
        self.df['year'] = self.df[self.column].dt.year
        self.df['month'] = self.df[self.column].dt.month
        self.df['day'] = self.df[self.column].dt.day
        self.df = self.df.drop(columns=self.column)

        return self.df
