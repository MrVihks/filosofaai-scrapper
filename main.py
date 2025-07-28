import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.pensador.com/nietzsche/")
soup = BeautifulSoup(res.content, "html.parser")


quotes = soup.find_all("p",class_="frase fr")

for quote in quotes:
    print(quote.get_text())