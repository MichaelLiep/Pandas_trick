# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 45: Memadukan loc dan iloc untuk melakukan seleksi data

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
print(df.head())

# Memadukan loc dan iloc untuk melakukan seleksi data
print(df.iloc[15:20, :].loc[:, 'name':'age'])
print(df.loc[:, 'name':'age'].iloc[15:20, :])


# 46: Seleksi weekdays dan weekends pada data deret waktu (time series)

# Persiapan Data Frame
n_rows = 365
n_cols = 2
cols = ['col1', 'col2']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')
print(df.head())

# Seleksi weekdays dan weekends
weekdays_df = df[df.index.dayofweek.isin([0, 1, 2, 3, 4])]
print(weekdays_df.head(7))

weekends_df = df[df.index.dayofweek.isin([5, 6])]
print(weekends_df.head(7))


# 47: Deteksi dan penanganan kolom dengan tipe data beragam (mixed data types)

# Persiapan Data Frame
d = {
    'nama': ['bejo', 'tejo', 'wati', 'tiwi', 'cecep'],
    'ipk': [2, '3', 3, 2.75, '3.25']
}
df = pd.DataFrame(d)
print(df)

# Deteksi dan penanganan kolom dengan tipe data beragam
print(df.dtypes)

print(df['ipk'].apply(type))
print(df['ipk'].apply(type).value_counts())

df['ipk'] = df['ipk'].astype(float)

print(df['ipk'].apply(type).value_counts())


# 48: Mengenal Cummulative Count dengan cumcount()

# Persiapan Data Frame
d = {
    'penjual': ['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'],
    'barang': ['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']
}
df = pd.DataFrame(d)
print(df)

# Mengenal Cummulative Count dengan cumcount()
df['count_tiap_penjual'] = df.groupby('penjual').cumcount() + 1
print(df)

df['count_tiap_barang'] = df.groupby('barang').cumcount() + 1
print(df)

df['count_pasangan_kolom'] = df.groupby(['penjual', 'barang']).cumcount() + 1
print(df)