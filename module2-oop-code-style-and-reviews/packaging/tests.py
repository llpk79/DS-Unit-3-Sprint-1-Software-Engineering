from helper.add_column import AddColumn
from helper.separate_date_parts import SeparateDateParts
from helper.delete_columns import DeleteColumn
from helper.display import DisplayOptions
import pandas as pd

# Make a DataFrame for testing.
df = pd.DataFrame({'strings': ['yes', 'no', 'maybe'],
                   'nums': [1, 2, 4],
                   'floats': [.1, .3, .5],
                   'dates': ['2018-9-29', '2017-12-30', '2019-1-25']})

# Make a new column to add.
new = [4, 6, 3]

# Test out our new functions! Woot!
df = AddColumn(df, new, 'ints').add_column()
print(df)

df = SeparateDateParts(df, 'dates').parse_dates()
print(df)

df = DeleteColumn(df, 'nums').delete_column()
print(df)

DisplayOptions(max_columns=50)
