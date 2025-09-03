x = [ 90,56,34,23,93,76]
while True:
    swapped = False
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            swapped =True
    if not swapped:
         break
print(x)