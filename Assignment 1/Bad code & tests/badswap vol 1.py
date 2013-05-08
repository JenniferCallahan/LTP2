def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    
    L[:k], L[-k:] = L[-k:], L[:k

                              
    #head,tail = L[:k],L[-k:]
    #for n in range(k):
    #    L.pop(0)
    #for n in range(k):
    #    L.pop()
    #for k in head:
    #    L.append(k)
    #tail.reverse() -- will cause test case to return [6, 5, 3, 4, 1, 2]
    #for l in tail:
    #    L.insert(0,l)
    ## FFFF.F


    #for i in range(k):
        # we should save L[i] before assigning it, but we don't
     #   L[i] = L[-i]
        # so this sets L[-i] to exactly what is was previously
      #  L[-i] = L[i]
        # now end of string overwrites beginning of string
    ## F.FEFFFF. -- index error for empty list; fails -- test 1, test 2,
    ## general case even & odd, half even & odd

    #start_swap = L[0:k]
    #L[0:k] = L[-k:] #put the end swap part in the place of the start swap
    #L[-k:] = start_swap; #replace the end swap part with the saved start swap
    ## .F......F -- fails 1-item list and k == 0

    #for a in range(k):
    #    temp = L[a]
    #    L[a] = L[a -k - 1]
    #    L[a -k - 1] = temp
    #    # buggy. Indexes are erroneous
    # ...E..... -- fails empty list, gives index out of range

    #for i in range(k):
    #    temp = L[i]
    #    L[i] = L[i + k]
    #    L[i + k] = temp
    ## F..EFF.F. -- empty list = index error; fails 1 change, general case even & odd
    ## half_odd    

    
    #temp = 0
    #for index in range (k):
    #    temp = L[index]
    #    L[index] = L[len(L) - k + index]
    #    L[len(L) - k + index] = temp
    ## ...E..... -- fails empty list; gives index out of range error
    
    #(L[0:k], L[-k:]) = (L[-k:], L[0:k])
    ## .F......F -- fails single-item and k == 0

    #for i in range(k):
    #    temp = L[i]
    #    #changes pairs of items instead of first and last blocks
    #    L[i] = L[-i-1]
    #    L[-i-1] = temp
    ## ...EFFFF. -- gives index out of range error for empty list; fails
    ## general case even & odd, and half even & odd

    # indexing error
    #if k>len(L)//2 or k<=0:
    #    L=L
    #else:
    #    swapped_list = []
    #    swapped_list.extend(L[-k:])
    #    swapped_list.extend(L[k+1:-k-1])
    #    swapped_list.extend(L[:k])
    #    L.clear()
    #    L.extend(swapped_list)
    ## E.E.EEEE. -- author claims this is an indexing error, but for all Es, I get
    ## list object has no attribute 'clear' -- same below

    #if k>len(L)//2 or k<=0:
    #    L=L
    #else:
    #    swapped_list = []
    #    swapped_list.extend(L[-k:])
    #    swapped_list.extend(L[k:-k])
    #    swapped_list.extend(L[:k])
    #    L.clear()
    #    L.extend(swapped_list)
    #return L
    ## E.E.EEEE.
