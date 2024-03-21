from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url="https://en.wikipedia.org/wiki/Lists_of_stars"

page=requests.get(bright_stars_url)
print(page)

soup=bs(page.text,'html.passer')
star_table=soup.find('table')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    tem_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(0,len(tem_list)):
    star_names.append(tem_list[i][1])
    distance.append(tem_list[i][3])
    mass.append(tem_list[i][5])
    radius.append(tem_list[i][6])
    lum.append(tem_list[i][7])

data_frame=pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_names','Distance','Mass','Radius','Luminosity'])
print(data_frame)

data_frame.to_csv('bright_stars.csv')


    

