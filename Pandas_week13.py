# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

# 49: Seleksi kolom menggunakan f-string

# Persiapan Data Frame
df = pd.read_csv('./data/Iris.csv')
print(df.head())

# Seleksi kolom dengan f-string 
print(df['SepalWidthCm'].to_frame().head())

part = 'Sepal'
print(df[f'{part}WidthCm'].to_frame().head())

print(df[['PetalWidthCm', 'PetalLengthCm']].head())

part = 'Petal'
print(df[[f'{part}WidthCm', f'{part}LengthCm']].head())


# 50: Membuat kolom baru dengan looping dan f-string

# Persiapan Data Frame
d = {
    'penjual': ['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'], 
    'barang': ['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']
}

df = pd.DataFrame(d)
print(df)

# Membuat kolom baru dengan for loop dan f-string
cols = ['penjual', 'barang']

for col in cols:
    df[f'count_tiap_{col}'] = df.groupby(col).cumcount() + 1

print(df)


# 51: Seleksi baris dengan between()

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

# Seleksi baris dengan between()
print(df[df['A'].between(2, 5)])
print(df[df['A'].between(2, 5, inclusive='neither')])


# 52: Transformasi kolom menjadi baris pada Data Frame

# Persiapan Data Frame
d = {
    'kode_area': [123, 456, 789, 321],
    'pabrik': [4, 2, 5, 0],
    'gudang': [2, 4, 7, 3],
    'toko': [64, 32, 15, 24]
}

df = pd.DataFrame(d)
print(df)

# Transformasi kolom menjadi baris
df = df.melt(
    id_vars='kode_area',
    var_name='jenis_bangunan',
    value_name='jumlah'
)

print(df)