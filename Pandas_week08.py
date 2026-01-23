# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)
print(np.__version__)

# 29: Melakukan random sampling pada Data Frame

# Persiapan Data Frame
d = {
    'col_1': [1, 2, 3, 4, 5],
    'col_2': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(d)
print(df)

# Random sampling with/without replacement
print(df.sample(n=4, replace=False, random_state=0))
print(df.sample(n=4, replace=True, random_state=0))


# 30: Akses nilai variable pada query()

# Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

# Akses nilai variabel pada query()
print(df.query('A > 5'))

rerata = df['A'].mean()
print(rerata)

print(df.query('A > @rerata'))


# 31: Mengenal tipe data ordinal pada Pandas

# Persiapan Data Frame
d = {
    'pelanggan': [11, 12, 13, 14],
    'kepuasan': ['baik', 'cukup', 'buruk', 'cukup']
}
df = pd.DataFrame(d)
print(df)

# Tipe data ordinal pada Pandas
from pandas.api.types import CategoricalDtype

tingkat_kepuasan = CategoricalDtype(
    ['buruk', 'cukup', 'baik', 'Sangat baik'],
    ordered=True
)

df['kepuasan'] = df['kepuasan'].astype(tingkat_kepuasan)
print(df)

df = df.sort_values('kepuasan', ascending=True)
print(df)

print(df[df['kepuasan'] > 'cukup'])


# 32: Plotting dari suatu Pandas Data Frame

# Persiapan Data Frame
n_rows = 40
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

print(df.head())

# Line Plot
df.plot(kind='line')
plt.show()

df[['A', 'B']].plot(kind='line')
plt.show()

# Bar Plot
df.plot(kind='bar')
plt.show()

df[['A', 'B']].plot(kind='bar')
plt.show()

df[['A', 'B']].head().plot(kind='bar')
plt.show()

df[['A', 'B']].head().plot(kind='barh')
plt.show()

# Area Plot
df.plot(kind='area')
plt.show()

df[['A', 'B']].head().plot(kind='area')
plt.show()

# Box Plot
df.plot(kind='box')
plt.show()

# Histogram
df.plot(kind='hist')
plt.show()

df[['A', 'B']].plot(kind='hist')
plt.show()

# Kernel Density Estimation (KDE)
df.plot(kind='kde')
plt.show()

# Scatter Plot
df.plot(x='A', y='B', kind='scatter')
plt.show()