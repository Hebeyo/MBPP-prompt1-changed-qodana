def add_dict(d1,d2):
    add_dict = {}
    for key in d1:
        if key in d2:
            add_dict[key] = d1[key] + d2[key]
        else:
            add_dict[key] = d1[key]
    for key in d2:
        if key not in add_dict:
            add_dict[key] = d2[key]
    return add_dict
