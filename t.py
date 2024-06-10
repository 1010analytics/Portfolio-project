import pandas as pd
import requests as re
response = re.get(input("mention url : "))
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

#Note_1 :- This is user defined URL, so by mentioning URL this will lead your defined URL web page.
#Note_2 :- There are some known and standard tags are mentioned in the below code in which by entering 
#          appropiate class, you can extract suitable dta.

# Note_3:- Mention the class for span tag from the user defined URL and extract suitable data.
box= soup.find_all("span", class_=input("mention the class_name : "))
list_1=[]
for i in box:
    boxes= i.text
    list_1.append(boxes)
print(list_1)

#Note_4:- This is standards tags for extracting all links from any web pages, so this can be used as it is.
link= soup.find_all("a")
list_2=[]
for j in link:
    links= j.get("href")
    list_2.append(links)
print(list_2)

# Note_5:- Mention the class for p tag from the user defined URL and extract suitable data.
Description =soup.find_all("p",class_=input("mention the class_name : "))
list_3=[]
for k in Description:
    desc= k.text
    list_3.append(desc)
print(list_3)

# Note_6:- Mention the class for a tag from the user defined URL and extract suitable data.
content_data =soup.find_all("a",class_=input("mention the class_name : "))
list_4=[]
for n in content_data:
    content= n.text
    list_4.append(content)
print(list_4)

# This are few known tags which exists in all HTML code, if URL HTML code contains any differnt tags,
# then by following above same code procedure, data can be extract.


# Exporting data from pandas to excel :-

df= pd.DataFrame({input("enter the name for list_1 : "): "list_1",
                  input("enter the name for list_2 : "): "list_2",
                  input("enter the name for list_1 : "): "list_3",
                  input("enter the name for list_1 : "): "list_4"})

print(df)

# we can further add more keys, depends on the tags, more u extract tags more will be keys added in df.

df.to_csv("Extracted_data.csv")