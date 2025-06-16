import pandas as pd

# List
buah = ['apel', 'jeruk', 'mangga', 'pisang']
print(buah)

a = pd.Series(buah, index=['1', '2', '3', '4'])
print(a)


# Dictionary
data_mhs = {
    'nama' : ['Budi', 'Siti', 'Andi'],
    'umur' : [20, 21, 22],
    'jurusan' : ['TI', 'SI', 'MI']
}

print(data_mhs)
data_mhs_df = pd.DataFrame(data_mhs)
print(data_mhs_df)