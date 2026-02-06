from pydantic import BaseModel

class Location(BaseModel):
    name: str
    location: str

class Company(BaseModel):
    name: str
    location: Location

data = {
    "name": "Widget",
    "location": {
        "name": "Headquarters",
        "location": "New York"
    }
}

company_obj = Company(**data)
print(company_obj.location.name)



c = [1,2,3,4,5]
even = filter(lambda x: x%2==0, c)
print(list(even))

mapfunc = [1,4,6,7,8]
result = map(lambda x: x*2, mapfunc)
print(list(result))

cars = [
    {"model": "Toyota Camry", "year": 2020, "price": 24000},
    {"model": "Honda Accord", "year": 2019, "price": 22000},
    {"model": "Ford Mustang", "year": 2021, "price": 35000}
]
sorted_cars = filter(lambda car: car["price"] > 10000, cars)
print(list(sorted_cars))

mapped_cars = map(lambda car: car["model"], cars)
print(list(mapped_cars))

filtered_cars = filter(lambda sample : sample["model"] == "Toyota Camry",cars)
print(list(filtered_cars))