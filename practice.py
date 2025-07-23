def Sumofa(arr):
    sum=0
    i=0
    e=len(arr)-1
    while(i<=e):
        sum+=arr[i]
        i+=1
    return sum
arr=[]
d=Sumofa(arr)
print(d)    