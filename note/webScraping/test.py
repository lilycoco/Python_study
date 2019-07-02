from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1.Get a html.
with urlopen("https://gsacademy.tokyo/mentor/") as res:
  html = res.read().decode("utf-8")

# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")

# 3. Get items you want.
# titles = soup.find_all("span")
# titles = soup.find_all(class_="pri")
# titles = [t.text for t in titles]

titles = soup.find_all("div")
titles = soup.find_all(class_="heading")
titles = soup.find_all("img")
titles = [t["src"] for t in titles]

#Check results.
from pprint import pprint
pprint(titles[:4])
