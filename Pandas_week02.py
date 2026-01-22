# Michael Liep Haryanto
# 2473037

# 05: Membalik urutan baris dan kolom pada Data Frame

import pandas as pd
import numpy as np

print("Pandas:", pd.__version__)
print("Numpy :", np.__version__)

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)

print("\nData Frame Awal:")
print(df)

# Membalik urutan kolom
print("\nMembalik urutan kolom:")
print(df.loc[:, ::-1])

# Membalik urutan baris
print("\nMembalik urutan baris:")
print(df.loc[::-1])

# Membalik urutan baris dan melakukan penyesuaian ulang index
print("\nMembalik baris + reset index:")
print(df.loc[::-1].reset_index(drop=True))


# 06: Mengganti nama (label) kolom pada Data Frame

import pandas as pd
import numpy as np

print("\nPandas:", pd.__version__)
print("Numpy :", np.__version__)

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)

print("\nData Frame Awal:")
print(df)

# Mengganti nama (label) untuk sebuah kolom pada Data Frame
print("\nGanti satu kolom (C menjadi Hobi):")
print(df.rename(columns={'C': 'Hobi'}))

# Mengganti nama (label) untuk banyak kolom pada Data Frame
print("\nGanti banyak kolom:")
print(df.rename(columns={'A': 'Nama', 'B': 'Alamat', 'D': 'Kota'}))


# 07: Menghapus (drop) missing values (NaN)

import pandas as pd

print("\nPandas:", pd.__version__)

df = pd.util.testing.makeMissingDataFrame().reset_index()
df = df.rename(columns={'index': 'Z'})

print("\nData Frame dengan Missing Values:")
print(df.head())

df_backup = df.copy(deep=True)

# Menghapus setiap kolom yang mengandung missing values
print("\nDrop kolom yang mengandung NaN:")
print(df.dropna(axis='columns').head())

# Menghapus setiap baris yang mengandung missing values
print("\nDrop baris yang mengandung NaN:")
print(df_backup.dropna(axis='rows').head())

# Persentase missing values untuk tiap kolom
print("\nPersentase missing values tiap kolom:")
print(df_backup.isna().mean())

# Menghapus kolom berdasarkan threshold
threshold = len(df_backup) * 0.9
print("\nDrop kolom berdasarkan threshold:")
print(df_backup.dropna(thresh=threshold, axis='columns').head())


# 08: Memeriksa kesamaan antar dua buah kolom (Series) pada Data Frame

import pandas as pd
import numpy as np

print("\nPandas:", pd.__version__)
print("Numpy :", np.__version__)

data = {
    'A': [15, 15, 18, np.nan, 12],
    'B': [15, 15, 18, np.nan, 12]
}

df = pd.DataFrame(data)

print("\nData Frame:")
print(df)

# Mengenal Pandas Series
print("\nKolom A (Series):")
print(df['A'])

print("\nTipe df['A']:", type(df['A']))
print("Tipe df     :", type(df))

# Memeriksa kesamaan dengan operator ==
print("\nPerbandingan A == B:")
print(df['A'] == df['B'])

# Memeriksa kesamaan dengan method equals()
print("\nApakah A sama dengan B? (equals):")
print(df['A'].equals(df['B']))

# Memeriksa kesamaan antar dua Data Frame
df1 = df.copy(deep=True)

print("\nApakah df sama dengan df1?")
print(df.equals(df1))

print("\nPerbandingan df == df1:")
print(df == df1)