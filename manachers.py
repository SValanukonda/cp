# manacher is a linear algo to find all sub palindrome in a string 


s="aaba"
original=s
s=list(s)
s="#"+"#".join(s)+"#"
n=len(s)
odd=[0 for _ in range(n)]

#odd[i] length of span on both sides from center i , aba odd[1]=1 

#issuse with manacher is implementing for palindrome of length odd is easy
# when it comes to even is very hard to implement 0
# this always looks in back direction 

l=r=0
for i,j in enumerate(s):
    if(i<r):
        odd[i]=min(r-i,odd[l+(r-i)])
    while(i-odd[i]-1>=0 and i+odd[i]+1<n and s[i-odd[i]-1]==s[i+odd[i]+1]):
        odd[i]+=1
    if(i+odd[i]>r):
        l=i-odd[i]
        r=i+odd[i]
 


# now both even length and odd length both will be in same array
for i in range(len(original)):
    print(f"even at {i} = {2*odd[2*i]//2}")
    print(f"odd at {i} = {2*odd[2*i+1]//2}")
