def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0.10, -0.01])
    (0.14, -0.17)
    """
    ## ***********
    #gains = 0
    #losses = 0
    #for price in price_changes :
    #    if price <= 0 :
    #        losses = losses + price
    #    else:
    #        gains = gains + price
    #return (gains, losses)
    ## ***********
    ## this works but supposedly shouldn't
    ## this is not a Python version issue -- passes all tests in 2.7 as well

    #pos = 0.0
    #neg = 0.0
    #for price in price_changes:
    #    if price > 0:
    #        pos = pos + price
    #    elif price < 0:
    #        neg = neg + price
    #return pos, neg
    ## passes all 



    #gains_sum, losses_sum = 0 , 0
    #for i in range(len(price_changes)):
    #    if price_changes[i] >= 0:
    #        gains_sum+=price_changes[i]
    #    else:
    #        losses_sum+=price_changes[i]
    #return (round(gains_sum,2), round(losses_sum,2))
    ## appears to work

    #tuple_1 = 0
    #tuple_2 = 0
    #for i in price_changes:
    #    if i >= 0:
    #        tuple_1=round((tuple_1 + i),2)
    #    else:
    #        tuple_2=round((tuple_2 + i),2)
    #return (tuple_1,tuple_2)
    ## appears to work




   # sumGain = 0.00
    #sumLosses = 0.00
    #for i in price_changes:
    #    if i <0.00:
    #        sumLosses = sumLosses + i
    #    sumGain = sumGain + i
    #return (sumGain, sumLosses)
    ## FF....


    #gain, loss = 0, 0       
    #for price_change in price_changes:
    #    if price_change >= 0:        
    #        gain += price_change
    #    else:            
    #        loss -= price_change
    #return (gain, loss)
    ## FF.... long mixed & negative, short-mixed

    #gains,losses = 0,0
    #for n in price_changes:
    #    if n < 0:
    #        losses += n
    #    else:
    #        gains += n
    ##return (gains,losses) -- correct return line
    #return (losses,gains)
    ## FF.F..

    #loss_list = []
    #gain_list = []
    #for item in price_changes:
    #    if item < 0:
    #        loss_list.append(round(item))
    #    else: 
    #        gain_list.append(round(item))
    #losses = sum(loss_list)
    #gains = sum(gain_list)
    #return (gains, losses)
## FF.F.. -- failed long mmixed, negative, & positive

    #gains = losses = 0
    #for n in price_changes:
    #    if n > 0:
    #        gains = gains + n
    #    else:
    #        losses = losses + n
    # buggy, 'cause the tuple is in the wrong order
    #return losses, gains
## FF.F. -- fails long mixed, negative, and positive

    #var1 = 0
    #var2 = 0
    #if price_changes==[]:
    #    return 'your list is empty'
    #else:
    #    for v in price_changes:
    #      if v > 0 :
    #          var1 = var1 + v          
    #      else :
    #          var2 = var2 + v
    #    return {(var1, var2)}
    ## FFFF. -- fails long mixed, negative, none, positive

    #gains = 0
    #losses = 0
    #for price in price_changes:
    #    if price < 0:
    #        gains += price
    #    else:
    #       losses += price
    #buggy, gains and losses are swapped
    #return gains, losses
    ##.FFFF -- fails long-mixed, short-mixed, negative, positive

    
   
   # total_gain = 0.00
   # total_loss = 0.00
   # for change in price_changes :
   #     if change == 0.00 :
   #         break
   #     elif change > 0.00 :
   #         total_gain += change
   #     else :
   #         total_loss += change
   #  return (total_gain, total_loss)
   ## F....

   
   # result = [0.0,0.0]
   # for price in price_changes:
   #    result[int(price<0)] += price
   # return result
   ## FFFF. -- fails long mixed, negative, none, and positive

   # gains = loses = 0
   # for changes in price_changes:
   #     if changes > 0:
   #         gains = gains + changes
   #     else:
   #         # subtraction instead of sum
   #         loses = loses - changes
   # return gains, loses
   ## FF... fails long mixed & negative

   
