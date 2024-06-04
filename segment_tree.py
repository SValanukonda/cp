
arr = [5,8,6,3,2,7,2,6]
print(arr)
length=len(arr)
# segtree with len of 2*n (n is len of arr should be 2 power) uses one based indexing 
#for i left node will be segtree[2*i] and right node will be segtree[2*i+1]
segtree=[0]*(2*length)


#creating segtree

#initialize all leaf nodes 
for i in range(len(arr)):
    segtree[i+length]=arr[i]

#creating all parent nodes
for i in reversed(range(length)):
    segtree[i]=segtree[2*i]+segtree[2*i+1]





#range query
# if  strtindex%2=0 means it is left node so we dont add it and move to parent meaning increase
# if strtindex%2=1 means it is right so we need to add/include into answer
# if endindex%2=1 means it is right node so we dont add/include into answer and decrease it move to parent
# if endindex%2=0 means it is left node so we have to add/include it into answer 

def rangequery(a,b):
    ans=0
    a+=length
    b+=length
    while(a<=b):
        if(a%2==1):
            ans+=segtree[a]
            a+=1 
        if(b%2==0):
            ans+=segtree[b]
            b-=1 
        a//=2
        b//=2
    return(ans)



def normalquery(a,b):
    ans=0
    for i in range(a,b+1):
        ans+=arr[i]
    return(ans)
print(segtree)

print(rangequery(4,5),normalquery(4,5))