import math
def num_buses(n):

    ##************
    ## return math.ceil( n / 50 )
    ## supposedly this code should not pass -- it's the code we're using
    ## **********
    ## in Python 2.7, this code returns 0.0 for values <50, which is
    ## very different from its behavior in Python 3.x

    ## **********
    max_per_bus = 50
    min_buses = n // max_per_bus
    if min_buses  ==  n / max_per_bus:
       return min_buses
    else:
      return min_buses + 1
    ## ******************

    ## *****
    ## **************************************
    ## NEEDS A TEST TO ENSURE THAT RETURN VALUE IS INT
    #return math.ceil(n/50.0) #returns float
    ## I CAN'T MAKE THIS RETURN A FLOAT

    #if n < 1:
     #   return 0
    #else:
    #    return int(n//50.1 + 1)
    #...F.. fails test large if test case written to end in 1

    #if n!= 0 and n < 50 :
    #    return 1
    #if (n%50)== 0 :
    #    return int(n/50)
    #else :
    #    return n// 50 + 1
    # this appears to work


    #count = 0
    #while n >=0:
    #    n-= 50
    #    count += 1
    #if n > 0 :
    #    count += 1
    #return count
    ## F....F fails smallest & test_1_max

    #if n != 0 and (n % 50) != 0:
    #    num_buses = 1 + (n // 50)
    #if n != 0 and (n % 50) == 0:
    #    num_buses = (n // 50)
    #
    #return num_buses


    #bus_capacity = 50
    #return (n + bus_capacity) // bus_capacity
    #F....F

    #bus_capacity = 50
    #return (n // (bus_capacity + 1)) + 1
    #..F..F

    #bus_capacity = 50
    #return (n // bus_capacity) + 1
    #F....F

    #bus_capacity = 50
    #return n // (bus_capacity + 1)
    #FFFFF.

    #bus_capacity = 50
    #return n // bus_capacity
    #.FFFF.

    
    #if n > 0:
    #    bus_capacity = 50
    #    return math.ceil(n / bus_capacity)
    # .....F -- returns None when input is 0; fails smallest

    ## &&&&&&&&&&&&&&
    #return n//51+1
    ## ..F..F -- fails for n == 0, fails test_3 (101)
    

    #var = 1
    #if n <= 50 :
    #    return 1
    #elif n % 50 == 0 :
    #    return n / 50
    #else :         
    #      var= var + (n / 50)
    #return round(var,0)
    ## F.... -- fails n==0



    #buses = n // 50 + 1
    # buggy because of error when n is multiple of 50
    #return buses
    ## F..F. -- fails 0 and 50


    

   # var = 1
   # if n==0:
   #     return 0
   # if n <= 50 and not n==0:
   #     return 1
   # elif n % 50 == 0 :
   #     return n / 50
   # else :         
   #       var= var + (n / 50)
   # return var
    ## ..F.F -- fails 51 (gives 2.02) and 1020 (gives 21.4)
    
#    people_per_bus = 50
#    return n / people_per_bus + 1
# FFFF fails all 4 tests; 1 for 0, 1.02 for 1, 2 for 50, 2.02 for 51


    #if n > 0:
        #return math.ceil(n/50)
    # F. . . fails test input of 0 b/c it returns 'None'

    #if n > 0:
        #return math.ceil(n/50)
    #else:
        #return 1
    # F . . . fails test input of 0 b/c it returns 1
    
    #return math.floor(n/50)
# . F .F fails test with input of 1 b/c it returns 0; fails test with input of 51
# b/c it returns 1 -- anything not evenly divisible by 50 will fail

#buggy 5:
#def num_buses(n):
   # if n/50 == n//50:
    #    return n//50
    #else:
     #   return n//50 + 1
     #passes all 5 tests


    #L = [0]*50
    #i=0
    # error line: while n>=0:
    #while n>0: 
     #   L[i]+=1
        #error line: if n%50==0:
      #  if (n-1)%50==0 or i > 48:
       #     i=0
       # else:
        #    i+=1
        #n-=1       
    #return max(L)
# F..F. with error lines -- very strange use visualizer to see


 #    return n // 50 + 1
# F..F.


