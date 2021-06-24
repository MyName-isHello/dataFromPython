import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date
from time import sleep
from random import randint
from datetime import datetime
def timeNow():
	return datetime.now().strftime('%H:%M:%S') 

t = randint(0,600)
print(f"sleep {t}(s)  \n| NOW:{timeNow()}")
sleep(t)
print(f"sleep End \n| NOW:{timeNow()}\nstall now")

url = "https://www.macrotrends.net/stocks/stock-screener"

br = "######################################################"

rqe = requests.request("get",url)

soup = BeautifulSoup(rqe.text,"lxml")
match = soup.find("body",class_="fuelux")
#
# script = match.script # try 2020/8/28
register = str(match.script)

#print(str(script)[2])

cut = ""
for i in range(0,len(register)):
    if register[i] == "]":
        cut = register[0:i+1]
        break

for i in range(0,len(cut)):
    if cut[i] == "=":
        cut = cut[i+1:]
        break
print(f"| NOW:{timeNow()}\ndone")



# jsonCut = json.dump(cut,sort_keys=True)
#print(cut)


#print(cut)
day = date.today().strftime("%d/%m/%Y").replace("/", "-")




print(day)
# str(day)
format_0 = '.json'
format_1 = '.csv'

#location = "F:\dataFromPython\UsSymbol\DATA_" + day + format_0
#print(location)
#f = open(location,"w")
#f.write(cut)
#f.close()

df = pd.read_json(cut)
location = r'/home/wilson-pi/dataFromPython/UsSymbol/_pi_DATA_AUTO_' + day + format_1
df.to_csv(location,index=None)
print(f"| NOW:{timeNow()}")
