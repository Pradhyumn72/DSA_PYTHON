def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if (arr[i]==target):
            return arr[i]
    return -1
l1=[20,30,40,90,10]
target=40
result=linear_search(l1,target)
print(result)