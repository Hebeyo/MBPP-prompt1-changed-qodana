def count_Substrings(s,n):
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += ord(s[j]) - ord('0')
            if sum == j - i + 1:
                count += 1
    return count
