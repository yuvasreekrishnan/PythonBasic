class productData:
    id = 1
    title = "Sample Product"
    description = "This is a sample product description."
    price = 99.99
    discountPercentage = 10.0
    rating = 4.5
    stock = 50

    # def __init__(self):
    #     print("Product Data Initialized")
    #     print(self.description)

# productData1 = productData()
# productData1.title = "Updated Product Title"
# print(productData1.title)
# productData1.price = 79.99
# print(productData1.price)


    def __init__(self, id, title, description,category, price,discountPrice,rating, stock):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.price = price
        self.discountPrice = discountPrice
        self.rating = rating
        self.stock = stock

productData2 = productData(2, "New Product", "New product description", "Electronics", 199.99, 179.99, 4.7, 30)
print(productData2.title)