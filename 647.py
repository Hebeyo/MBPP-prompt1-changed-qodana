def split_upperstring(text):
    ans = []
    start = 0
    for i in range(1, len(text)):
        if text[i].isupper():
            ans.append(text[start:i])
            start = i
    ans.append(text[start:])
    return ans
