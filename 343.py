def dig_let(s):
    l = sum(1 for c in s if c.isalpha())
    d = sum(1 for c in s if c.isdigit())
    return (l, d)
