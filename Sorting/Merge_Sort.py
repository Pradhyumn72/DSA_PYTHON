def Merge(l1,s,m,e):
    i=s
    j=m+1
    ans=[]

    while(i<=m and j<=e):
        if(l1[i]<l1[j]):
            ans.append(l1[i])
            i+=1
        elif(l1[i]>l1[j]):
            ans.append(l1[j])
            j+=1
        elif(l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i+=1
            j+=1
    while(i<=m):
        ans.append(l1[i])
        i+=1
    while(j<=e):
        ans.append(l1[j])
        j+=1
    startofMyans=0
    startofMylist=s
    while(startofMylist<=e):
        l1[startofMylist]=ans[startofMyans]
        startofMyans+=1
        startofMylist+=1

    return
    
def MergeSortHelper(l1,s,e):
    if(s>=e):
        return
    m=s+(e-s)//2
    MergeSortHelper(l1,s,m)
    MergeSortHelper(l1,m+1,e)
    Merge(l1,s,m,e)
    return

def MergeSort(l1):
    return MergeSortHelper(l1,0,len(l1)-1)


l1=[111,121,132,140,90]
MergeSort(l1)
print(l1)