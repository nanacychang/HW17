import csv
import requests
from bs4 import BeautifulSoup

url='https://rate.bot.com.tw/xrt/quote/ltm/USD'

headers={'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64; x64) AppleWebkit/537.36(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

resp=requests.get(url, headers=headers)

resp.encoding='utf-8'

raw_html=resp.text

soup=BeautifulSoup(raw_html, "html.parser")

def str_to_float(raw_data):
  return float(raw_data.replace(',',''))

rate_list=[]

for index in range (1,10):
  print ('index',index)
  rate_dict={}
  rate_dict['date']=soup.select(f'#ie11andabove>div>table>tbody>tr:nth-child({index})>td:nth-child(1)>a')[0].text
  rate_dict['rate']=str_to_float(soup.select(f'#ie11andabove>div>table>tbody>tr:nth-child({index})>td:nth-child(3)')[0].text)  
  rate_list.append(rate_dict)
  print(rate_dict['date'],rate_dict['rate'])

headers=['date','rate']

with open('rate.csv','w') as rate_file:
   dict_writer=csv.DictWriter(rate_file, headers)
   dict_writer.writeheader()
   dict_writer.writerows(rate_list)
