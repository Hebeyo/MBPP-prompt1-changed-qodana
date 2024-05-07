def replace(string, char):
    new_string = ""
    for i in string:
        if i == char:
            if i != new_string[-1:]:
                new_string += i
        else:
            new_string += i
    return new_string
