import pandas as pd


class DisplayOptions(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def set_display(self):
        for key, val in self.kwargs:
            pd.set_option('display.' + key, val)
