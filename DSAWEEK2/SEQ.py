def seqsearch(L , item):
    i=0
    while i<  len(L):
        if L[i]  == item:
            return i
        i+=1
    return None

L = [1,2,3,4,5,6,7,8,9,0]
print(seqsearch(L,4))