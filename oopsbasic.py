class productInfo:
    id = 1
    title =""
    description = ""
    category = ""
    brand = "" 
    price = 100
    discountprice = 10
    stock = 1
product1 = productInfo()
print(product1.price)


class productData:
    id = 12
    title ="yuvasree"
    description = "new product"
    category = "good"
    brand = "insight" 
    price = 1800
    discountprice = 20
    stock = 50

    def __init__(self,id,title,description,category,brand,price,discountprice,stock):
     self.id = id
     self.title = title
     self.description = description
     self.category = category
     self.brand = brand
     self.price = price
     self.discountprice = discountprice
     self.stock = stock

productData1 = productData(12,"gomathi","new product","good","insight",1800,20,50)
print(productData.title)


