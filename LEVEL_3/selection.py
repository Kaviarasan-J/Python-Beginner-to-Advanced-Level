x = [56,37,68,47,79,32,67]
for i in range(len(x)):
    min_index = i
    for j in range(i+1,len(x)):
        if x[i] < x[min_index]:
            min_index = j
    x[i],x[min_index] = x[min_index],x[i]
print(x)