def extract_elements(numbers,n):
    result = []
    for i in range(len(numbers)-n+1):
        if numbers[i:i+n] == [numbers[i]]*n:
            result.append(numbers[i])
    return result
