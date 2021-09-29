# Given list of stock prices return best buy and sell spots

def best_price(prices):

    maxi = 0
    for i in range(len(prices)-1):
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j]:
                current = prices[j] - prices[i]
                if current > maxi:
                    maxi = current
                    start = prices[i]
                    end = prices[j]
    if maxi == 0:
        return None
    else:
        return 'The max is ' + str(maxi) + ' starting at ' + str(start) + ' and ending at ' + str(end)


print(best_price([1, 5, 10, 9, 15, 8]))