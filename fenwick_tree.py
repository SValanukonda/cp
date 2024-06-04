#!!!!!!! NOTE !!!!!!!!!!
# nums list follows 0 based indexing
# bit list follows 1 based indexing
n = 20
nums = list(range(1,n+1))
bit = [0 for _ in range(n+1)]


# this update function adds delta value to every parent
def update(pos,delta):
   while(pos<=n):
       bit[pos]+=delta
       pos +=pos&-pos
      
      
# calling update function for each input
def build_by_update (nums):
    for i,j in enumerate(nums):
        update(i+1,j)
     
# this sum travells tres from given point to leafs to get prefix sum
def tsum (endPos):
    ans = 0
    while(endPos>0):
        ans+=bit[endPos]
        endPos -= endPos&-endPos
    return(ans)
    

# there is a linear algo for bit list initialization
def linear_build(nums):
    for i,j in enumerate(nums):
        i+=1
        bit[i]+=j
        prnt = i+(i&-i)
        if(prnt<=n): bit[prnt]+=bit[i]

#build_by_update(nums)
linear_build(nums)
print(nums)
print(len(nums))
print(bit)
print(len(bit))
print(tsum(20))
update(20,5)
print(tsum(20))