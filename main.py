from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = bs(page.text, 'html.parser')

star_table = soup.find_all('table')
print(len(star_table))


temp_list = []
table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)


Star_names = []
Distance = []
Mass = []
Radius = []


for i in range(1, len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    try:
        Distance.append(float(temp_list[i][5]))
    except:
        pass
    try:
        Mass.append(float(temp_list[i][7]))
    except:
        pass
    try:
        Radius.append(float(temp_list[i][8]))
    except:
        pass

df = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius,)), columns=[
                   'Star_name', 'Distance', 'Mass', 'Radius'])
# print(df)

df.to_csv('2.csv')
df = df.dropna()
print('\n \n ', df.dtypes)
