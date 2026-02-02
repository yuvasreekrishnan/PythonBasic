sample = (100,200,300,400)
print(type(sample))

temp_sample = list(sample)
print(temp_sample)
print(type(temp_sample))

temp_sample[0] = 111
print(temp_sample)

sample = tuple(temp_sample)
print(sample)
print(type(sample))

sample = sample + (500,600)
print(sample)

sample += (700,)
print(sample)

sample1 = (800,900,1000)
sample1 = (1100,1200,1300)
print(sample1)

for i in range(len(sample)):
    print(sample[i])

for x in sample:
    if(x==800):
     print("the third element is:",x)
else:
        print("the loop is ended")  