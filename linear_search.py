def linear_search(list1,n,key):
    for i in range (0,n):
        if(list1[i] == key):
            return i
    return -1

list1 = [10,4,32,1,54,3,2,90]
n = len(list1)
res = linear_search(list1,n,90)
if(res==-1):
    print("Element not found")
else:
    print("Element found at position ",res+1)
    
