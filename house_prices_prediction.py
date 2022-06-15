
from selenium import webdriver
#from BeautifulSoup import BeautifulSoup

from bs4 import BeautifulSoup
import pandas as pd

# To configure webdriver to use Chrome browser, we have to set the path to chromedriver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


price=[] #List to store name of the product
room=[] #List to store price of the product
city=[] #List to store rating of the product
location=[] 
driver.get("https://bina.az/baki/alqi-satqi/menziller/yeni-tikili/2-otaqli?items_view=list")


content = driver.page_source
soup = BeautifulSoup(content)

# card_params

for a in soup.findAll('a',href=True, attrs={'class': "items"}): 
    price=a.find('div', attrs={'class':"price-val"})
    location=a.find('div', attrs={'class':"location"})
    name=a.find('div', attrs={'class':"name"})
    date=a.find('div', attrs={'class':"city_when"})
                    

    price.append(name.price)
    location.append(location.text)
    name.append(name.text) 
    date.append(date.text) 

    
df = pd.DataFrame({'Price':price,'Location':location, 'Date':date}) 
df.to_csv('houses.csv', index=False, encoding='utf-8')