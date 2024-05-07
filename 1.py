def min_cost(cost, m, n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(min_cost(cost, m-1, n-1), min_cost(cost, m-1, n), min_cost(cost, m, n-1))
