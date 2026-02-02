sample = [10,20,30,40,50]
print(sample)

sample.append(60)
print(sample)  

print(len(sample))
print(sample[2])

sample2 = [100,200,300,400,500]
# sample.extend(sample2)
# print(sample)

sample = sample + sample2
print(sample)

sample.insert(0,5)
print(sample)

print(sample.index(300))

print(sample[len(sample)-1])

print(sample.count(100))

print(sample.clear())
print(sample)











