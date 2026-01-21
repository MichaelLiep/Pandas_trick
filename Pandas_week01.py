# Michael Liep Haryanto
# 2473037

# 01: Menyertakan Prefix dan Suffix pada seluruh Kolom Data Frame

# Import Modules
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# Persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 10, size=(n_rows, n_cols)),
    columns=cols
)

print("\nData Frame Awal:")
print(df)

# Menyertakan Prefix Kolom
print("\nData Frame dengan Prefix:")
print(df.add_prefix('kolom_'))

# Menyertakan Suffix Kolom
print("\nData Frame dengan Suffix:")
print(df.add_suffix('_field'))


# 02: Pemilihan baris (rows selection) pada Data Frame

# Import Modules
import pandas as pd
import numpy as np

print("\n", pd.__version__)
print(np.__version__)

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 5, size=(n_rows, n_cols)),
    columns=cols
)

print("\nData Frame:")
print(df)

# Selection dengan operator logika |
print("\nBaris dengan nilai A = 1 atau 3:")
print(df[(df['A'] == 1) | (df['A'] == 3)])

# Selection dengan fungsi isin()
print("\nBaris dengan nilai A termasuk [1, 3]:")
print(df[df['A'].isin([1, 3])])

# Mengenal operator negasi ~
print("\nBaris dengan nilai A bukan 1 atau 3:")
print(df[~df['A'].isin([1, 3])])


# 03: Konversi tipe data String ke Numerik pada kolom Data Frame

# Import Modules
import pandas as pd

print("Pandas:", pd.__version__)

# Persiapan Data Frame
data = {
    'col1': ['1', '2', '3', 'teks'],
    'col2': ['1', '2', '3', '4']
}
df = pd.DataFrame(data)

print("\nData Frame Awal:")
print(df)

print("\nTipe Data Awal:")
print(df.dtypes)

# Konversi tipe data dengan fungsi astype()
df_x = df.astype({'col2': 'int'})

print("\nData Frame setelah astype():")
print(df_x)

print("\nTipe Data setelah astype():")
print(df_x.dtypes)

# Konversi tipe data numerik dengan fungsi to_numeric()
print("\nKonversi dengan to_numeric (errors='coerce'):")
print(df.apply(pd.to_numeric, errors='coerce'))


# 04: Pemilihan kolom (columns selection) pada Data Frame berdasarkan tipe data

# Import Modules
import pandas as pd
import numpy as np

print("\nPandas:", pd.__version__)
print("Numpy :", np.__version__)

# Persiapan Data Frame
n_rows = 5
n_cols = 2
cols = ['bil_pecahan', 'bil_bulat']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pd.date_range(start='2024-01-01', periods=n_rows, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE')

print("\nData Frame:")
print(df)

print("\nTipe Data Kolom:")
print(df.dtypes)

# Memilih kolom bertipe data numerik
print("\nKolom bertipe numerik:")
print(df.select_dtypes(include='number'))

print("\nKolom bertipe float:")
print(df.select_dtypes(include='float'))

print("\nKolom bertipe int:")
print(df.select_dtypes(include='int'))

# Memilih kolom bertipe data string atau object
print("\nKolom bertipe object/string:")
print(df.select_dtypes(include='object'))

# Memilih kolom bertipe data datetime
print("\nKolom bertipe datetime:")
print(df.select_dtypes(include='datetime'))

# Memilih kolom dengan kombinasi tipe data
print("\nKolom bertipe number dan object:")
print(df.select_dtypes(include=['number', 'object']))