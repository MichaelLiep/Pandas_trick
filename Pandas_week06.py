# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 21: Melakukan agregasi menggunakan agg()

# Persiapan Data Frame
df = pd.read_csv('./data/Iris.csv')
print(df.head())

# Mengenal groupby() dan fungsi agregasi
print(df.groupby('Species')['PetalLengthCm'].count().to_frame())
print(df.groupby('Species')['PetalLengthCm'].mean().to_frame())
print(df.groupby('Species')['PetalLengthCm'].median().to_frame())

# Agregasi dengan agg()
print(df.groupby('Species')['PetalLengthCm'].agg(['count', 'mean', 'median']))

# Agregasi dengan describe()
print(df.groupby('Species')['PetalLengthCm'].describe())


# 22: Memantau penggunaan memory suatu data frame

# Persiapan Data Frame
df_titanic = pd.read_csv('./data/titanicfull.csv')
print(df_titanic.head())

df_iris = pd.read_csv('./data/Iris.csv')
print(df_iris.head())

# Memantau penggunaan memory suatu data frame
df_titanic.info(memory_usage='deep')
df_iris.info(memory_usage='deep')

# Memantau penggunaan memory untuk setiap kolom dari suatu data frame
print(df_titanic.memory_usage(deep=True))
print(df_iris.memory_usage(deep=True))


# 23: Seleksi baris pada Data Frame dengan query()

# Persiapan Data Frame
d = {
    'kolom_satu': [1, 2, 3, 4, 5],
    'kolom dua': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(d)
print(df)

# Seleksi baris dengan query()
print(df.query('kolom_satu > 2'))
print(df.query('`kolom dua` > 30'))


# 24: UTC dan konversi zona waktu (time zone) pada python pandas

# Persiapan Series
s = pd.Series(range(1591683521, 1592201921, 3600))
s = pd.to_datetime(s, unit='s')
print(s.head())

# Pengaturan zona waktu (time zone)
s = s.dt.tz_localize('UTC')
print(s.head())

s = s.dt.tz_convert('Asia/Jakarta')
print(s.head())

s = s.dt.tz_convert('Australia/Hobart')
print(s.head())