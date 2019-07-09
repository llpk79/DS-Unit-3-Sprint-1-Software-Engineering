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

```
  strings  floats  ints  year  month  day  ints
0     yes     0.1     4  2018      9   29     4
1      no     0.3     6  2017     12   30     6
2   maybe     0.5     3  2019      1   25     3

```
## Delete a column from a DataFrame.

### Use like this:
```
from helper.delete_columns import DeleteColumn

df = DeleteColumn(df, 'nums').delete_column()
```
```  
  strings  nums  floats  ints  year  month  day
0     yes     1     0.1     4  2018      9   29
1      no     2     0.3     6  2017     12   30
2   maybe     4     0.5     3  2019      1   25
```
## Separate dates into year, month and day columns.

### Use like this:
```
from helper.separate_date_parts import SeparateDateParts

df = SeparateDateParts(df, 'dates').parse_dates()
```
```
  strings  floats  ints  year  month  day
0     yes     0.1     4  2018      9   29
1      no     0.3     6  2017     12   30
2   maybe     0.5     3  2019      1   25

```