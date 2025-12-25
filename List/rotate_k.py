# Rotate List by K Steps
a = [1,2,3,4,5]
k = 7
k = k % len(a)
def reverse( strt , end ):
    while strt < end:
        tmp = a[strt]
        a[strt] = a[end]
        a[end] = tmp
        strt+=1
        end-=1
reverse(0 , len(a) - 1)
reverse( 0 , k-1)
reverse( k ,  len(a) - 1)

print(a)

# [4, 5, 1, 2, 3]