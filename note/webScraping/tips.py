# 要素選択

# select
soup.select(".articleListItem h2")

# find
soup.find("h1")
soup.find(id="header_subtitle")
soup.find(class_="articleListItem")

#find_all
soup.find_all("h2")
soup.find_all(id="header_subtitle")
soup.find_all(class_="pubDate")


# 値を取得する

# text
# <h1>My Special App</h1>
elm.string

# attribute
# <img src="/my_secret.png"/>
elm["src"]