sampleset = {"hi","hello","welcome","family"}
print(type(sampleset))
print(sampleset)

sampleset.add("newitem")
print(sampleset)

sampleset.remove("hi")
print(sampleset)

sampleset.update(["item1","item2","item3"])
print(sampleset)



lenovo = {"ryzen","windows","16gb","512ssd"}
dell = {"intel","windows","8gb","1tb"}

union = lenovo | dell
print(union)

intersection = lenovo & dell
print(intersection)

difference = lenovo - dell
print(difference)

difference2 = dell - lenovo
print(difference2)

symmetric_difference = lenovo ^ dell
print(symmetric_difference)

list = ["a","b","c","d"]
newset = set(list)
print(newset)
print(type(newset))
newlist = list(newset)
print(newlist)  
print(type(newset)) 

