def text_starta_endb(text):
    import re
    patterns = 'a.*b$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
