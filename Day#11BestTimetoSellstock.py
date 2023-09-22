def maxProfit(prices) -> int:
    l,res=0,0
    for r in prices:
        print(r,prices[l])
        if prices[l] > r :
            l=prices.index(r)
            print(prices[l])
        res =max(res,r-prices[l])
    print(res)

maxProfit([2,1,2,1,0,1,2])

"""sumary_line

Sliding window
Q121
"""
