# move zero to last
a = [0,1,0,3,12]
i = 0
j = 0

while j < len(a):
    if a[j] != 0: 
        a[i] , a[j] = a[j] , a[i]
        i+=1
    j+=1
print(a)

# [1, 3, 12, 0, 0]