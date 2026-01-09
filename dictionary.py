my_purchase = {
    "item": "handbag",
    "price": 79.99,
    "currency": "USD",
    "quantity": 1
}
print(my_purchase)

print(type(my_purchase))

print(my_purchase["item"])
print(my_purchase.get("price"))

my_purchase.pop("currency")
print(my_purchase)

my_purchase.popitem()
print(my_purchase)


print(my_purchase.keys())
print(my_purchase.values())
print(my_purchase.items())

my_purchase["item"] = "backpack"
print(my_purchase)

bikeinfo = {}
bikeinfo["brand"] = "dio"
print(bikeinfo)

bikeinfo.update({"model":"zx","year":2020,"color":"red","price":150000
                 })
print(bikeinfo)

bikeinfo.update(price = 140000)
print(bikeinfo)
