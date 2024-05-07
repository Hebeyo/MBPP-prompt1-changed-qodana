def camel_to_snake(text):
    # import re
    # str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    # return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
    res = ''.join(['_'+i.lower() if i.isupper() else i for i in text]).lstrip('_')
    return res