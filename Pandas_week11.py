# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 41: Menerapkan agregasi pada sejumlah kolom dengan agg()

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
print(df.head())

# Menerapkan agregasi pada sejumlah kolom dengan agg()
print(
    df.groupby('pclass').agg({
        'pclass': 'count',
        'age': ['mean', 'max'],
        'survived': 'mean'
    })
)

print(
    df.groupby('pclass').agg(
        n_pass=('pclass', 'count'),
        avg_age=('age', 'mean'),
        max_age=('age', 'max'),
        survival_rate=('survived', 'mean')
    )
)


# 42: Mengurutkan data berdasarkan kolom tertentu

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
print(df.head())

# Mengurutkan data berdasarkan kolom tertentu
print(df.sort_values('age').head())

print(df.sort_values('age', ascending=False).head())

print(df.sort_values(['survived', 'age']).head())


# 43: Menangani whitespace pada Data Frame

# Persiapan Data Frame
data = {
    'nim': ['10', '11', '12', '13', '  '],
    'nama': ['adi', '  ', 'tejo', '  ', 'bejo']
}

df = pd.DataFrame(data)
print(df)

print(df.info())

df = df.replace(r'^\s*$', np.nan, regex=True)
print(df)

print(df.info())


# 44: Menata ulang penempatan kolom pada Data Frame

# Persiapan Data Frame 
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

# Menata ulang penempatan kolom pada Data Frame
print(df[['D', 'C', 'A', 'E', 'B']])

print(df)

df = df[['D', 'C', 'A', 'E', 'B']]
print(df)