# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print("Pandas:", pd.__version__)
print("Numpy :", np.__version__)


# 09: Membagi Data frame menjadi dua secara acak

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols)

print("\nData Frame Awal:")
print(df)

# Membagi Data Frame menjadi dua secara acak berdasarkan proporsi tertentu
proporsi = 0.7
df_1 = df.sample(frac=proporsi, random_state=1)
df_2 = df.drop(df_1.index)

print(f"\ndf_1 shape: {df_1.shape}")
print(df_1)

print(f"\ndf_2 shape: {df_2.shape}")
print(df_2)


# 10: Mengganti nama (label) kolom pada Data Frame berdasarkan pola

# Persiapan Data Frame
df = pd.DataFrame({
    'Pclass': [1, 2, 3],
    'Survival status': [1, 0, 1],
    'full name': ['A', 'B', 'C'],
    'sex ': ['male', 'female', 'female'],
    ' age': [20, 30, 25]
})

print("\nData Frame Awal:")
print(df)

# Menggunakan lowercase untuk nama kolom dan mengganti spasi dengan _
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

print("\nNama kolom setelah dirapikan:")
print(df.columns)


# 11: Melakukan seleksi kolom dan baris pada Data Frame menggunakan loc

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

print("\nData Frame:")
print(df)

# Seleksi kolom dan baris menggunakan loc
print("\nSeleksi baris 0,3,4 dan kolom B,E:")
print(df.loc[[0, 3, 4], ['B', 'E']])

# Seleksi baris dengan kondisi
print("\nSeleksi baris dengan kondisi B > 10:")
print(df.loc[df['B'] > 10, ['B', 'D', 'E']])

# Slicing Data Frame dengan loc
print("\nSlicing baris 0–4 dan kolom B–D:")
print(df.loc[0:4, 'B':'D'])


# 12: Membentuk kolom bertipe datetime dari sejumlah kolom lain pada Data Frame

# Persiapan Data Frame
data = {
    'day':   [1, 2, 10, 25, 12],
    'month': [1, 2, 3, 4, 5],
    'year':  [2000, 2001, 2010, 2015, 2020]
}

df = pd.DataFrame(data)

print("\nData Frame Awal:")
print(df)

# Membentuk kolom bertipe datetime
df['penanggalan'] = pd.to_datetime(df[['day', 'month', 'year']])

print("\nData Frame dengan kolom datetime:")
print(df)

print("\nTipe data kolom:")
print(df.dtypes)