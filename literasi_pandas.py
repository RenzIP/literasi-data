import pandas as pd

# # List
# buah = ['apel', 'jeruk', 'mangga', 'pisang']
# print(buah)

# a = pd.Series(buah, index=['1', '2', '3', '4'])
# print(a)


# # Dictionary
# data_mhs = {
#     'nama' : ['Budi', 'Siti', 'Andi'],
#     'umur' : [20, 21, 22],
#     'jurusan' : ['TI', 'SI', 'MI']
# }

# print(data_mhs)
# data_mhs_df = pd.DataFrame(data_mhs)
# print(data_mhs_df)
# print(data_mhs_df.head())
# print(data_mhs_df.tail())
# print(data_mhs_df.info())
# print(data_mhs_df.describe())
# print(data_mhs_df[['nama']])
# print(data_mhs_df.loc[0,'nama']) 
# print(data_mhs_df.iloc[0,0])


# dic = {
#     'A': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
#     'B': [751, 752, 753, 754, 755, 756, 757, 758, 759, 760],
#     'C': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# }

# latihan = pd.DataFrame(dic)
# print(latihan['A'])
# print(latihan.loc[3, 'B':'C'])  # Mengakses nilai pada baris ke-3 kolom 'A'
# print(latihan.head(4))

# dic2 = {
#     'D': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# }

# latihan2 = pd.DataFrame(dic2)
# print(latihan2['D'])

# merge = pd.concat([latihan, latihan2], axis=1)
# print(merge)

# data = pd.read_csv('austin_weather.csv')
# print(data)
# print (data['TempHighF'])

data_pomokit = pd.read_json('pomokit.json')
print(data_pomokit)