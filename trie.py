

#syntax [isend,numberofwordsending,childNodes]
trie=[False,0,dict()]


def insert(trie,word):
    node=trie
    #dfs on trie
    for i in word:
        if(i not in node[2]):
            node[2][i]=[False,0,dict()]
        node[1]+=1
        node=node[2][i]
    node[0]=True  #set ending Flag true 
    node[1]+=1  #increment count of ending word 


def search(trie,word):
    node=trie
    for i in word:
        if(i not in node[2]):
            return(False)
        node = node[2][i]
    return(True)


def isprefix(trie,word):
    node = trie
    for i in word:
        if(i not in node[2]):
            return(False)
        node=node[2][i]
    return(True)


def count(trie,word):
    node = trie
    for i in word:
        if(i not in node[2]):
            return(0)
        node=node[2][i]
    return(node[1])




insert(trie,"apple")
insert(trie,"abble")
insert(trie,"apple")
insert(trie,"apple")
print(count(trie,"ab"))