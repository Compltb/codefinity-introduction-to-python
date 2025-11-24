# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = "Bubblegum"
candy2 = "Chocolate"
dry_goods = "Pasta"
category1 = "Candy Aisle"
category2 = "Pasta Aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:28]
aisle1 = category1[0:11]
aisle2 = category2[0:11]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
price1 = bubblegum_price[0:5]
price2 = chocolate_price[0:5]
price3 = pasta_price[0:5]
print(candy1," ", candy2," ", dry_goods," ",aisle1," ",aisle2," ",price1," ",price2,"and",price3)

print("We have" + " " + candy1 + " for " + price1 + " in the " + aisle1)
print("We have" + " " + candy2 + " for " + price2 + " in the " + aisle1)
print("We have" + " " + dry_goods + " for " + price3 + " in the " + aisle2)