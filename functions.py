'''seve data in file'''
# https://www.proxy-list.download/api/v1/get?type=https

def save(data):
    open('done.txt', 'a+').write(data + '\n')


def apoi(addres, protocol):
    from requests import get
    try:
        if get('http://google.com', proxies={protocol : addres}):
            save(addres)
    except:
        pass


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

