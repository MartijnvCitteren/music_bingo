
import pandas as pd

xlsx_path = 'titel_artiest_example.xlsx'
column_names = ['title', 'artist']
df = pd.read_excel(xlsx_path, header=None, names=column_names)
print(df)
