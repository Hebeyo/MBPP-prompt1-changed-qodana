def remove(list): 
    for i in range(len(list)): 
        list[i] = ''.join([j for j in list[i] if not j.isdigit()]) 
    return list
