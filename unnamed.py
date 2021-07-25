# input=(10,20,30)
# output=[10,30,50]

data = (10,20,30)
a = []
a.append(data[0])
for i in range(1,len(data)):
    sum = data[i] +data[i-1]
    a.append(sum)
print(a)