def find_Sum(arr,n): 
    sum = 0
    for i in range(0,n): 
        if arr.count(arr[i]) > 1: 
            sum += arr[i] 
    return sum
