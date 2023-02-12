def bubble_sort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
        print(list1)


list1 = [23,4,1,3,22,45,0]  
bubble_sort(list1)


