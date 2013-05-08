lst = [1 ,2, 3, 4, 5, 6,]
stng = lst[0:60]
stng2 = lst[1:3]
stng3 = lst[10:30]
print (stng)
#this prints [1, 2, 3, 4, 5, 6]
print (stng2)
# this prints [2,3]
print (stng3)
# this prints []

def jacked(L): 
    index = 1
    for item in L: 
        print (L[index])
        index = index + 1
    
lst = [1,2,3]
jacked(lst)

# this gives Error index out of range as soon as 
# index = 3