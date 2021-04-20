'''seve data in file'''
# https://www.proxy-list.download/api/v1/get?type=https
working = 0
working_proxies = []


def save(data):
    f = open('./done.txt', 'a+')
    f.write(data + '\n')
    f.close()

# --- ^ = + = ^ --- #
def apoi(addres, protocol):
    from requests import get

    global working
    global working_proxies
    
    if protocol != 'http':
        url = 'https'
    else:
        url = 'http'
    if protocol == 'socks4' or protocol == 'socks5':
        protocol = 'socks'

    try:
        if get(url + '://google.com', proxies={protocol : addres}, timeout=10):
            working_proxies.append(addres)
            working += 1
    except:
        pass
# --- ^ = + = ^ --- #


def check(addres):
    from proxy_checker import ProxyChecker

    global working
    global working_proxies

    if ProxyChecker().check_proxy(addres) != False:
        working_proxies.append(addres)
        working += 1



def writa():
    import json
    from cfg import json_file

    if json_file:
        with open('done.json', 'a+') as j_file:
            json.dump(working_proxies, j_file)

    for x in working_proxies:
        file = open('./done.txt', 'a+')
        file.write(x + '\n')
        file.close()


def cutter(addres):
    sd = False
    port = ''
    ip = ''

    for x in addres:
        if x == ':':
            sd = True
        continue

    if sd == False:
        ip += x

    else:
        port += x

    return addres, port
