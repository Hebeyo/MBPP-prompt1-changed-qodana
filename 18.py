def remove_dirty_chars(string, second_string): 
    for i in second_string: 
        string = string.replace(i, '') 
    return string
