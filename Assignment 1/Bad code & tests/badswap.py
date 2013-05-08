def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

   # n = len(L) - 1
   # rev = L
   # count = 0
    # Transpose items at beginning of L with those at end
    #while count + 1 <= k: 
    #      rev.count = L[n - count]
    #      rev[n - count] = L.count
    #      count = count + 1

    # Return L as rev
    #L = rev 

    beginning = L[0:k]
    ending = L[-k:]
    L[0:k] = ending
    L[-k:] = beginning
    ## .F......F fails 1-item & no change

    #right=L[-k:]
    #left=L[:k]
    #for i in range(k):
    #    L[i]=right[i]
    #for i in range(k):
    #    L[len(L)-i-1]=left[len(left)-i-1]
    ##...E..... -- empty list
    
    ##L[:k], L[-k:] = L[-k:], L[:k]
    ## .F......F

    #for i in range(k):
    #    L[i], L[-1-i] = L[-1-i], L[i]
    ## ...EFFFF. gives index error for empty list; fails general even & odd,
    ## half even & odd

    #if 0 <= k <= len(L) // 2:
      #  holder = L[0:k]
       # L[0:k] = L[-k:]
       # L[-k:] = holder
       # return L
    ## .F......F

    #new_list=L[:k]
    #for i in L :
    #    for j in range(k):
    #        L[j] = L[-1-j]
    #for o in new_list:
    #    for g in range(k):
    #        L[-1-g]=new_list[g]
    ## ....FFFF.

