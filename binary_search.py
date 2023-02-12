def binary_search(list1, low, high, key):
    if high >= low:
        mid = (high + low) // 2

        if list1[mid] == key:

            return mid

        elif list1[mid] > key:
            return binary_search(list1, low, mid - 1, key)
        else:
            return binary_search(list1, mid + 1, high, key)

    else:
        return -1
    
list1 = [10,23,45,53,57,75]
low = 0
high = len(list1)-1
key =45
res = binary_search(list1, low , high, key)
if res==-1:
    print("Element not found")
else:
    print("Element found at",res)
    
