def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    mid=(start+end)//2
    while (start<=end):
        if (arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            start=mid+1
        elif (arr[mid]>target):
            end=mid-1