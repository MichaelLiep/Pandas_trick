# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 37: Seleksi baris dengan banyak kriteria

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')

# Seleksi baris dengan banyak kriteria
print(
    df[
        (df['sex'] == 'female') &
        (df['age'] >= 60) &
        (df['embarked'] == 'S') &
        (df['survived'] == 1)
    ]
)

print(
    df[
        (df['sex'] == 'female') &
        (df['age'] >= 60) &
        (df['embarked'] == 'S') &
        (df['survived'] == 1)
    ]
)

kr1 = df['sex'] == 'female'
kr2 = df['age'] >= 60
kr3 = df['embarked'] == 'S'
kr4 = df['survived'] == 1

print(df[kr1 & kr2 & kr3 & kr4])


# 38: Mengenal parameter header dan skiprows

# Persiapan Data Frame
df = pd.read_csv('./data/iris_error.csv')
print(df.head(8))

df = pd.read_csv('./data/iris_error.csv', header=2, skiprows=[5, 6])
print(df.head())


# 39: Mengacak urutan baris pada DataFrame

# Persiapan Data Frame
n_rows = 6
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 5, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

# Mengacak urutan baris pada DataFrame
print(df.sample(frac=1.0, random_state=1))
print(df.sample(frac=1.0, random_state=1).reset_index(drop=True))


# 40: Mengakses sekelompok data dengan get_group()

df = pd.read_csv('./data/titanicfull.csv')
print(df.head())

# Mengakses sekelompok data yang sudah terkelompok dengan get_group()
grouped_df = df.groupby('sex')
print(grouped_df.get_group('female').head(10))

grouped_df = df.groupby('survived')
print(grouped_df.get_group(1).head(10))