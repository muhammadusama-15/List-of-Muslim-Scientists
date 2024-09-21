#Importing required packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Getting the html text from the required webpage
response = requests.get("https://en.wikipedia.org/wiki/List_of_scientists_in_medieval_Islamic_world")
webpage = response.text

#Creating a soup to scrap the data
soup = BeautifulSoup(webpage, "html.parser")

#Creating a dictionary containing all the scientists and links for their webpages
scientists = soup.find_all(name="a", class_="mw-redirect")
scientists_dict = {scientist.getText():"https://en.wikipedia.org"+scientist.get("href") for scientist in scientists}

#Creating a dictionary in the required format and removing the unrequired data
all_scientists_names = []
all_scientists_url = []
for (key,value) in scientists_dict.items():
    if key == "ISBN":
        break
    else:
        all_scientists_names.append(key)
        all_scientists_url.append(value)

all_scientists = {"Serial No": [i+1 for i in range(len(all_scientists_names))],
                  "Names":all_scientists_names,
                  "URL":all_scientists_url}


#Creating a dataframe from the dictionary
dataframe = pd.DataFrame.from_dict(all_scientists)

#Saving the data in a '.csv' file
dataframe.to_csv("muslim_scientists.csv", index=None)
print("File Successfully Saved.")