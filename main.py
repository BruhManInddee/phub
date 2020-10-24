import requests
from bs4 import BeautifulSoup

url = "https://www.pornhub.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")
for link in links:
    href = str(link.get("href"))
    if href.startswith("/view") and href[-1].isdigit():
      response = requests.get("https://pornhub.com"+href)
      html = response.text
      soup = BeautifulSoup(html, "html.parser")
      links = soup.findAll('title')
      for link in links:
        with open("vids.txt","r") as file:
          sentence = str(link)[7:len(link)-9]+" - https://pornhub.com"+str(href)
          if sentence not in file.read():
            with open("vids.txt","a") as file:
              file.write(sentence)
              file.write("\n")

          
