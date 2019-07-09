# Some very basic DataFrame helper functions.

Start with a DataFrame.

```
import pandas as pd


df = pd.DataFrame({'strings': ['yes', 'no', 'maybe'],
                   'nums': [1, 2, 4],
                   'floats': [.1, .3, .5]})
```
## Add a new column to a DataFrame from a python list.

### Use like this:
```
from helper.add_column import AddColumn

# Make a list to add as a column to df.            
new = [4, 6, 3]

df = AddColumn(df, new, 'ints').add_column()
print(df.head())
```

## Delete a column from a DataFrame.

### Use like this:
```
from helper.delete_columns import DeleteColumn

df = DeleteColumn(df, 'nums').delete_column()
```

## Separate dates into year, month and day columns.

### Use like this:
```
from helper.separate_date_parts import SeparateDateParts

df = SeparateDateParts(df, 'dates').parse_dates()
```