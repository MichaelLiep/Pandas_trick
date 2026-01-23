# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print("Pandas:", pd.__version__)
print("Numpy :", np.__version__)

# 13: Konversi nilai numerik ke dalam sejumlah kategori

# Persiapan Data Frame 
n_rows = 10
n_cols = 1
cols = ('Usia',)

df = pd.DataFrame(
    np.random.randint(1, 99, size=(n_rows, n_cols)),
    columns=cols
)
print("\nData Usia:")
print(df)

# Pengelompokkan nilai numerik ke dalam beberapa kategori menggunakan cut()
df['Kelompok_usia'] = pd.cut(
    df['Usia'],
    bins=[0, 18, 65, 99],
    labels=['anak', 'dewasa', 'manula']
)
print("\nKelompok Usia:")
print(df)


# 14: Menggabungkan (merge) dua Data Frame

# Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print("\nData Frame Awal:")
print(df)

df1 = df.drop([1, 4])
df2 = df.drop([0, 3])

# Menggabungkan dua Data Frame
df_inner = pd.merge(df1, df2, how='inner')
print("\nInner Merge:")
print(df_inner)

df_outer = pd.merge(df1, df2, how='outer')
print("\nOuter Merge:")
print(df_outer)


# 15: Memecah nilai string dari suatu kolom ke dalam beberapa kolom baru

# Persiapan Data Frame
data = {
    'nama': ['Didi Kempot', 'Glen Fredly', 'Mbah Surip'],
    'Tempat_kelahiran': [
        'Surakarta, Jawa Tengah',
        'Jakarta, DKI Jakarta',
        'Mojokerto, Jawa Timur'
    ]
}

df = pd.DataFrame(data)
print("\nData Nama:")
print(df)

# Memecah nama depan dan nama belakang
df[['nama_depan', 'nama_belakang']] = df['nama'].str.split(' ', expand=True)

# Memecah nama Kota dan Provinsi
df[['Kota', 'Provinsi']] = df['Tempat_kelahiran'].str.split(', ', expand=True)
print("\nHasil Pemecahan Kolom:")
print(df)


# 16: Menata ulang Data Frame dengan multiple indexes menggunakan unstack()

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
print("\nData Titanic:")
print(df.head())

# Data Frame dengan multiple indexes dari hasil grouping
grouped = df.groupby(['sex', 'pclass'])['survived'].mean()

# Menata ulang Data Frame dengan multiple indexes
df_unstack = grouped.unstack()
print("\nHasil Unstack:")
print(df_unstack)