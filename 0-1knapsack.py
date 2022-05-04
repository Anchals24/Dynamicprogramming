#Problem statement:
"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item or dont pick it (0-1 property).
"""
#Input sample:
"""
Input
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
"""
#Output sample:
"""
Output: 3
"""


#Function to return max value that can be put in knapsack of capacity W.

#Method1: Using recursive approach[Brute-Force]

def knapSack(W, wt, val, n):
    """brute-force/ naive approach: will check each and every possibility using recursion."""
    #base case
    if n == 0 or W == 0:
        return 0
    #recursive code
    #if an item in the bag is greater than the size of bag.
    if wt[n-1] > W:
    #we cannot pick the item 
        return knapSack(W, wt, val, n-1)
    #if an item in the bag is equal to/lesser than the size of bag.
    elif wt[n-1] <= W:
        #either we can pick the item or we can not pick the item.
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

wt = [4,5,1]
val = [1,2,3]
n = 3
W = 4
knapSack(W,wt,val,n)

#Method2: Using Recursion + Memoization[DP] ->> optimized approach

def helper(W, wt, val, n, DP):
    if n == 0 or W == 0:
        return 0
    if DP[n][W] != -1:
        return DP[n][W]
    if wt[n-1] <= W:
        DP[n][W] = max(val[n-1]+ helper(W-wt[n-1], wt, val, n-1,DP), helper(W,wt,val,n-1,DP))
        return DP[n][W]
    elif wt[n-1] > W:
        DP[n][W] = helper(W,wt,val,n-1,DP)
        return DP[n][W]


def knapSack(W, wt, val, n):
    """ 
        In prev recursive code, we noticed W and n were changing. 
        Let's take a matrix for the same. 
        taking n+1 rows and W+1 columns to prevent calling the recursive function over and over again.
    """  
    DP = []
    for row in range(n+1):
        for column in range(W+1):
            columns = [-1] * (W+1)
            DP.append(columns)
        
    return helper(W, wt, val, n, DP)

wt = [4,5,1]
val = [1,2,3]
n = 3
W = 4
knapSack(W,wt,val,n)


#Method3: Using tabulation(Iterative approach) -> DP -> Optimized

def knapSack(W, wt, val, n):
    #taking n+1 rows and W+1 columns for tabulation.
    DP = []
    for row in range(n+1):
        for column in range(W+1):
            columns = [-1] * (W+1)
            DP.append(columns)
    
    #initialization(equivalent to the base condition in recursive code)
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                DP[i][j] = 0
    #filling the remaining ones.
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                DP[i][j] = max(val[i-1]+DP[i-1][j-wt[i-1]], DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]
    return DP[n][W]








