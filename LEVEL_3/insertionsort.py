x = [ 90,56,34,23,93,76]

for i in range(1,len(x)):
    cur = x[i]
    j = i-1
    while j >= 0 and cur < x[j]:
        x[j+1] = x[j]
        j-= 1
    x[j+1] = cur
print(x)