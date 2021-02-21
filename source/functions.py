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
    for x in working_proxies:
        file = open('./done.txt', 'a+')
        file.write(x + '\n')
        file.close()


# Получение прокси через api + проверка

'''
def check_api_proxy(cycle):
    from requests import get
    for x in range(cycle):
        info = get('https://api.getproxylist.com/proxy')
        if get('google.com', proxies={info['protocol'] : str(info['ip']: info['port'])}):
            save(str(info['ip'] + ':' + info['port']))
'''
'''
def check_file(what, l, ):
    from requests import get
    done_list = []
    if len(l) % 2 != 0:
        number_of_proxies = int((len(l) - 1) / 2)
    else:
        number_of_proxies = int(len(l) / 2)

    if what == 1:
        scout = l[:number_of_proxies]
    else:
        scout = l[number_of_proxies:]
    for x in range(number_of_proxies):

        proxies = {'http': scout[x]}
        try:
            if get(url, proxies=proxies)

                done_list.append(scout[x])
            else:
                print('no')
        except Exception as e:
            print(e)
    print(done_list)
'''

