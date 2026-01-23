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
print(df.resample('ME')['col1'].sum().to_frame())

# Resampling data dengan interval daily
print(df.resample('D')['col1'].sum().to_frame())


# 18: Membentuk dummy Data Frame

# Membentuk Data Frame dari Dictionary
print(pd.DataFrame({'col1':[1,2,3,4],
                    'Col2':[5,6,7,8]}))

# Membentuk Data Frame dari Numpy Array
n_rows = 5
n_cols = 3

arr = np.random.randint(1,20,size=(n_rows,n_cols))
print(arr)

print(pd.DataFrame(arr, columns=tuple('ABC')))


# 19: Formatting tampilan Data Frame

# Persiapan Data Frame
n_rows = 5
n_cols = 2
cols = ['omset', 'operasional']

df = pd.DataFrame(
    np.random.randint(1,20,size=(n_rows,n_cols)),
    columns=cols
)

df['omset'] = df['omset'] * 100_000
df['operasional'] = df['operasional'] * 10_000

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='D')
df = df.reset_index()
df = df.rename(columns={'index':'tanggal'})
print(df)


# 20: Menggabungkan (merge) dua Data frame secara berdampingan

# Persiapan Data Frame
d1 = {'col1':[1,2,3],
      'col2':[10,20,30]}
df1 = pd.DataFrame(d1)

d2 = {'col1':[4,5,6],
      'col2':[40,50,60]}
df2 = pd.DataFrame(d2)

# Menggabungkan (merge) dua data frame secara berdampingan
df = pd.merge(df1, df2, left_index=True, right_index=True)
print(df)