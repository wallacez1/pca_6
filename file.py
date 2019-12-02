import pandas as pd


df = pd.read_excel('data.xlsx',encoding='utf-8')
df = df.dropna()
df.columns =  df.columns.str.strip()
del df['Ano_lançamento']
del df['Ano(Anderson)']

df.to_csv('data.csv',index=False,encoding='utf-8',sep=',')
