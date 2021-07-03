import pandas as pd
df = pd.read_csv("2.csv")
print(df.head())
print('\n \n \n \n \n', df.columns)
print('\n \n \n \n \n', df.dtypes)
df = df.dropna()
print('\n \n \n \n \n', df.dtypes)

df['Radius'] = df['Radius']
df["Radius"] = 0.102763*df["Radius"]

df['Mass'] = df['Mass']
df["Mass"] = 0.000954588*df["Mass"]

print(df.head())
print(df.columns)
# df.drop(['Unnamed: 0'], axis=1, inplace=True)
# df = df.drop("index", axis=1,inplace=True)
# del df[df.columns[0]]
# df.columns = [ "Star_name", "Distance", "Mass", "Radius"]
# df.drop(df.columns[df.columns.str.contains(
#     'unnamed', case=False)], axis=1, inplace=True)

# print(df.head())
df.reset_index(drop=True, inplace=True)

df.to_csv("merged.csv")

print(df.dtypes)
