def occurance_substring(text,pattern):
    for i in range(len(text)):
        if text[i:i+len(pattern)]==pattern:
            return (pattern,i,i+len(pattern))
        else:
            continue
    return None
