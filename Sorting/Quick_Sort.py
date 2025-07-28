def partition(l,s,e):
    pivot=l[e]
    i=s
    rp=s    #rp is right position
    
    while(i<=e-1):
        if(l[i]<pivot):
            rp+=1
        i+=1
    l[rp],l[e] = l[e],l[rp]
    pivotindex=rp

    # everything smaller to pivot on left and greater on right side
    start=s
    end=e
    while(start<pivotindex and end>pivotindex):
        if(l[start]<pivot):
            start+=1
        elif(start<pivotindex and end>pivotindex):
            end-=1
        else:
            l[start],l[end] =l[end],l[start]
            start+=1
            end-=1
        return pivotindex
def quicksort(l,s,e):
    if(s>=e):
        return
    pivotindex=partition(l,s,e)
    quicksort(l,s,pivotindex-1)
    quicksort(l,pivotindex,e)


l=[3,7,19,2,5,8]
quicksort(l,0,len(l)-1)
print(l)