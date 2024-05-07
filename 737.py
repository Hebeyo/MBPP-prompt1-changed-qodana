def check_str(string):
    import re
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    return "Valid" if re.search(regex, string) else "Invalid"
