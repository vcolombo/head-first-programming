import urllib.request
import time

def get_price():
  page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
  text = page.read().decode("utf8")
  where = text.find('>$')
  start_of_price = where + 2
  end_of_price = start_of_price + 4
  return(float(text[start_of_price:end_of_price]))


get_price_now = input("Get price immediately? (Y/N) ")

if get_price_now.upper() == "Y":
  print(get_price())
else:
  price = get_price()
  while price > 4.74:
    print("Not yet, the price is", str(price) + "!")
    time.sleep(10)
    price = get_price()
  print("The price is", str(price) + "!", "Buy!")
