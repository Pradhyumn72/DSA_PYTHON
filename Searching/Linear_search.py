def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if (arr[i]==target):
            return i 
    return -1
l1=[20,30,40,90,10]
target=40
rs=linear_search(l1,target)
print(rs)