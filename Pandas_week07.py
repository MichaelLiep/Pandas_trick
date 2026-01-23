# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 17: Resampling pada data deret waktu (time series data)

# Persiapan Data Frame
n_rows = 365 * 24
n_cols = 2
cols = ['col1', 'col2']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='h')
print(df.head())

# Resampling data dengan interval monthly
print(df.resample('ME')['col1'].sum().to_frame().head())

# Resampling data dengan interval daily
print(df.resample('D')['col1'].sum().to_frame().head())


# 18: Membentuk dummy Data Frame

# Membentuk Data Frame dari Dictionary
print(pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'Col2': [5, 6, 7, 8]
}))

# Membentuk Data Frame dari Numpy Array
n_rows = 5
n_cols = 3

arr = np.random.randint(1, 20, size=(n_rows, n_cols))
print(arr)
print(pd.DataFrame(arr, columns=tuple('ABC')))


# 19: Formatting tampilan Data Frame

# Persiapan Data Frame
n_rows = 5
n_cols = 2
cols = ['omset', 'operasional']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

df['omset'] = df['omset'] * 100_000
df['operasional'] = df['operasional'] * 10_000

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')
df = df.reset_index()
df = df.rename(columns={'index': 'tanggal'})

print(df)


# 20: Menggabungkan (merge) dua Data frame secara berdampingan

# Persiapan Data Frame
d1 = {'col1': [1, 2, 3], 'col2': [10, 20, 30]}
df1 = pd.DataFrame(d1)
print(df1)

d2 = {'col1': [4, 5, 6], 'col2': [40, 50, 60]}
df2 = pd.DataFrame(d2)
print(df2)

# Menggabungkan (merge) dua data frame secara berdampingan
df = pd.merge(df1, df2, left_index=True, right_index=True)
print(df)


# 21: Melakukan agregasi menggunakan agg()

# Persiapan Data Frame
df = pd.read_csv('./data/Iris.csv')
print(df.head())

# Mengenal groupby() dan fungsi agregasi
print(df.groupby('Species')['PetalLengthCm'].count().to_frame())
print(df.groupby('Species')['PetalLengthCm'].mean().to_frame())
print(df.groupby('Species')['PetalLengthCm'].median().to_frame())

# Agregasi dengan agg ()
print(df.groupby('Species')['PetalLengthCm'].agg(['count', 'mean', 'median']))

# Agregasi dengan describe()
print(df.groupby('Species')['PetalLengthCm'].describe())


# 22: Memantau penggunaan memory suatu data frame

# Persiapan Data Frame
df_titanic = pd.read_csv('./data/titanicfull.csv')
df_iris = pd.read_csv('./data/Iris.csv')

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

# Pengaturan zona waktu (time zone)
s = s.dt.tz_localize('UTC')
print(s.head())

s = s.dt.tz_convert('Asia/Jakarta')
print(s.head())

s = s.dt.tz_convert('Australia/Hobart')
print(s.head())


# 25: Pengaturan tampilan (display option) pada Python Pandas

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')

# Pengaturan tampilan
pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_colwidth', 20)

print(df.head())

pd.reset_option('^display.', silent=True)


# 26: Membuat Data Frame dari hasil seleksi Spreadsheet

# Membuat Data Frame dari hasil seleksi Spreadsheet
try:
    df = pd.read_clipboard()
    print(df)
except:
    pass


# 27: Mengenal fungsi agregasi first() dan last()

# Persiapan Data Frame
d = {
    'dokter': ['Budi', 'Wati', 'Iwan', 'Budi', 'Budi', 'Wati'],
    'pasien': ['Abdul', 'Rahmat', 'Asep', 'Joko', 'Wiwin', 'Lisa']
}

df = pd.DataFrame(d)
print(df)

# Mengenal fungsi agregasi first() dan last()
print(df.groupby('dokter')['pasien'].count().to_frame())
print(df.groupby('dokter')['pasien'].first().to_frame())
print(df.groupby('dokter')['pasien'].last().to_frame())


# 28: Mengenal explode dan implode list pada data frame

# Persiapan Data Frame
d = {
    'Team': ['DC', 'Marvel'],
    'Heroes': [
        ['Batman', 'Superman', 'Wonder Woman', 'Aquaman', 'Green Lantern', 'Shazam'],
        ['Iron Man', 'Captain America', 'Ant-Man', 'Black Panther', 'Captain Marvel']
    ]
}

df = pd.DataFrame(d)
print(df)

# Explode
df1 = df.explode('Heroes')
print(df1)

# Implode
df2 = pd.DataFrame({'Team': ['DC', 'Marvel']})
df2['Imploded'] = df1.groupby(df1.index)['Heroes'].agg(list)
print(df2)