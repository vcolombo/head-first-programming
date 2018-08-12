import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")

price = text[text.find(">$")+2:text.find(">$")+6]
print(price)
