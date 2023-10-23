from bs4 import BeautifulSoup
import requests
import re


#url ="https://www.newegg.com/global/uk-en/gigabyte-geforce-rtx-4070-gv-n4070aorus-m-12gd/p/N82E16814932612"

#prices = doc.find_all(text = "£")
#parent = prices[0].parent
#strong = parent.find("strong")
#sup = parent.find("sup")
#print("£"+ strong.string +sup.string)

#file changer
# with open ("index.html","r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags  = doc.find_all ("input",type="text")
# for tag in tags:
#     tag["placeholder"] = "Changedmmm"

# with open ("changed.html","w") as file:
#     file.write(str(doc))




# """crypto price finder"""
# url = "https://coinmarketcap.com/"
# result = requests.get(url).text
# doc = BeautifulSoup(result, "html.parser")

# tbody = doc.tbody
# trs  = tbody.contents

# prices = {}

# for tr in trs[:10]:
#     name,price = tr.contents[2:4]
#     fixed_name= name.p.string
#     fixed_price = price.a.string

#     prices[fixed_name] = fixed_price











"""newegg product finder"""


search_term = input("What product do you want to search for? ")

url =f"https://www.newegg.com/global/uk-en/p/pl?d={search_term}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page,"html.parser") 

page_text  = doc.find(class_="list-tool-pagination-text").strong
pages =int(str(page_text).split("/")[-2].split(">")[-1][:-1])


items_found = {}

for page in range(1,pages +1):
    url =f"https://www.newegg.com/global/uk-en/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page,"html.parser") 
   
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(string=re.compile(search_term))
    
    for item in items:
        parent = item.parent
        link = None
        if parent.name !="a":
            continue
        
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_ ="price-current").strong.string
            items_found[item] = {"price": int(price.replace(",","")),"link":link}
        except:
            pass
sorted_items = sorted(items_found.items(), key =lambda x: x[1]["price"])

for item in sorted_items:
    print(item[0])
    print(f"£{item[1]['price']}")
    print(item[1]["link"])
    print("-------------------------------------------------------------")

