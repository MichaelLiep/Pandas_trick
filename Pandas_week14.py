# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 53: Membuat kategori baru berdasarkan threshold (ambang batas)

# Persiapan Data Frame
d = {
    'hobi': [
        'jogging', 'mancing', 'renang',
        'mancing', 'mancing', 'baca',
        'baca', 'mancing', 'fotografi',
        'mancing', 'camping'
    ]
}

df = pd.DataFrame(d)
print(df)

# Membuat kategori baru berdasarkan threshold (ambang batas)
print(df['hobi'].value_counts())

persentase = df['hobi'].value_counts(normalize=True)
print(persentase)

threshold = 0.1
hobi_lain = persentase[persentase < threshold].index
print(hobi_lain)

df['hobi'] = df['hobi'].replace(hobi_lain, 'lainnya')
print(df['hobi'])

print(df['hobi'].value_counts(normalize=True))


# 54: Menyimpan Data Frame sebagai file CSV

# Persiapan Data Frame
data = {
    'nama': ['bejo', 'tejo', 'wati', 'tiwi', 'cecep'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L'],
    'umur': [20, 21, 19, 20, 22]
}

df = pd.DataFrame(data)
print(df)

# Menyimpan Data Frame sebagai file CSV
df.to_csv('data_peserta.csv', index=False)

df = pd.read_csv('data_peserta.csv')
df.to_csv('data_peserta_tanpa_index.csv', index=False)

print(df)

df = pd.read_csv('data_peserta_tanpa_index.csv')
print(df)


# 55: Menghitung jumlah baris menurut kriteria tertentu

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

print(df[df['A'] > 5].count())
print(df[df['A'] > 5].mean())


# 56: Mengeluarkan kolom dari Data Frame

# Persiapan Data Frame
data = {
    'nama': ['bejo', 'tejo', 'wati', 'tiwi', 'cecep'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L'],
    'umur': [20, 21, 19, 20, 22]
}

df = pd.DataFrame(data)

# Mengeluarkan kolom dari Data Frame
usia = df.pop('umur').to_frame()

print(df)
print(usia)