# Michael Liep Haryanto
# 2473037

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

# 33: Menampilkan nilai kumulatif 

# Persiapan Data Frame
d = {
    'pemain': ['Budi','Joni','Iwan','Budi','Iwan','Asep','Joni'],
    'goal': [2,1,3,1,1,2,3]
}
df = pd.DataFrame(d)
print(df)

# Menampilkan nilai kumulatif
print(df['goal'].cumsum().to_frame())

df['jumlah_goal_kumulatif'] = df['goal'].cumsum()
print(df)

df['jumlah_goal_kumulatif_tiap_pemain'] = df.groupby('pemain')['goal'].cumsum()
print(df)

df['cummax'] = df['goal'].cummax()
print(df)

df['cummin'] = df['goal'].cummin()
print(df)

df['cumprod'] = df['goal'].cumprod()
print(df)


# 34: Mapping pada Data Frame dengan applymap()

# Persiapan Data Frame
df = pd.DataFrame({
    'Jenis_klamin': ['Pria','Wanita','lelaki','perempuan','Pria'],
    'usia': [23,21,24,22,21],
    'shift': ['pagi','siang','malam','siang','pagi']
})
print(df)

# Mapping pada Data Frame dengan applymap()
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
print(df)

# applymap() dengan dictionary
mapping = {
    'pria': 'L',
    'lelaki': 'L',
    'wanita': 'P',
    'perempuan': 'P',
    'pagi': 1,
    'siang': 2,
    'malam': 3
}

df[['Jenis_klamin','shift']] = df[['Jenis_klamin','shift']].applymap(mapping.get)
print(df)


# 35: Memadukan fungsi agregasi dengan transform()

# Persiapan Data Frame
d = {
    'no_nota': [1,1,1,2,2,3,4,5],
    'kopi': ['latte','cappucino','latte','espresso','cappuccino','latte','espresso','latte'],
    'harga': [50,60,80,150,120,60,100,40]
}

df = pd.DataFrame(d)
print(df)

# Menghitung total harga untuk tiap nomor nota
print(df.groupby('no_nota')['harga'].sum().to_frame())

df['total_harga'] = df.groupby('no_nota')['harga'].transform('sum')
print(df)

# Menghitung total omset untuk tiap jenis kopi yang terjual
print(df.groupby('kopi')['harga'].sum().to_frame())

df['total_omset'] = df.groupby('kopi')['harga'].transform('sum')
print(df)


# 36: Menyatukan kolom dengan str.cat()

# Persiapan Data Frame
data = {
    'nama': ['Bayu','indra','devi','agni'],
    'Jenis_kelamin': ['L','L','P','L'],
    'usia': [23,21,22,25]
}

df = pd.DataFrame(data)
print(df)

# Menyatukan kolom dengan str.cat()
print(df['nama'].str.cat(df['Jenis_kelamin'], sep=',').to_frame())

df['nama_jk'] = df['nama'].str.cat(df['Jenis_kelamin'], sep=',')
print(df)

print(df['nama'].str.cat(df['usia'].astype(str), sep='-').to_frame())

df['nama_usia'] = df['nama'].str.cat(df['usia'].astype(str), sep='-')
print(df)