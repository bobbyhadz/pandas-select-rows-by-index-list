# Pandas: Select rows based on a List of Indices

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 180.2, 190.3, 205.5],
    'experience': [10, 15, 20, 25]
})

list_of_indices = [0, 2, 3]

new_df = df.iloc[list_of_indices]

#   first_name  salary  experience
# 0      Alice   175.1          10
# 2       Carl   190.3          20
# 3        Dan   205.5          25
print(new_df)