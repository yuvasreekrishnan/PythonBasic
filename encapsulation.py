class productData:
    id = 1
    __title = "Sample Product"
    description = "This is a sample product description."
    price = 99.99
    discountPercentage = 10.0
    rating = 4.5
    stock = 50

    def __init__(self, id, title, description,category, price,discountPrice,rating, stock):
        self.id = id
        self.__title = title
        self.description = description
        self.category = category
        self.price = price
        self.discountPrice = discountPrice
        self.rating = rating
        self.stock = stock


    def getTitle(self):
            # print(self.__title)
            return self.__title
        
    def setTitle(self, newTitle):
            self.__title = newTitle


productDatanew = productData(2, "New Product", "New product description", "Electronics", 199.99, 179.99, 4.7, 30)
# print(productDatanew.getTitle())

# productDatanew.setTitle("Updated Product Title")
# print(productDatanew.getTitle())
# print(productDatanew.__title)

if(productDatanew.getTitle()=="Updated Product Title"):
    productDatanew.setTitle("Final Product Title")
    print("Title updated successfully",productDatanew.getTitle())
else:
    print("Title update failed")
    print(productDatanew.getTitle())