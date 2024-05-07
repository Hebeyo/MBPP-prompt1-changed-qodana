def removezero_ip(ip):
    ip = ip.split('.')
    for i in range(0, len(ip)):
        ip[i] = str(int(ip[i]))
    return '.'.join(ip)
