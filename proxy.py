import threading
import time

import requests
import function

from o_cfg import *


work_proxy = []


def get_proxy(protocol): return requests.get(url + protocol).text


def only_proxy(proxy):
    proxy_list = []
    one_proxy = ''

    for x in proxy:
        if x != '\n':
            one_proxy += x
        else:
            one_proxy = one_proxy.replace('\r', '')
            proxy_list.append(one_proxy)
            one_proxy = ''

    return proxy_list


def check(proxy, protocol):
    global work_proxy

    if protocol == 'http' or protocol == 'https':
        answer = requests.get(f'{protocol}://google.com/',
                              proxies=dict(protocol=proxy), headers=heders, timeout=10)
        if answer:
            # function.ui.listWidget.addItem(proxy)
            work_proxy.append(proxy)
    else:
        http_proxy = dict(http=f'{protocol}://{proxy}')
        https_proxy = dict(https=f'{protocol}://{proxy}')

        http_answer = requests.get('http://google.com/',
                                   proxies=http_proxy, headers=heders, timeout=10)
        https_answer = requests.get('https://google.com/',
                                    proxies=https_proxy, headers=heders, timeout=10)
        if http_answer and https_answer:
            work_proxy.append(proxy)


def start_thread(proxy_list, protocol):
    for x in range(len(proxy_list)):
        while True:
            if threading.active_count() >= max_thread:
                time.sleep(sleep_time)
            else:
                break
        # function.ui.statusbar.showMessage(f'Начало тестирования {proxy_list[x]}')
        threading.Thread(target=check, args=(proxy_list[x], protocol)).start()


def viwe(list_text):
    out = ''
    for x in list_text:
        out += x + '\n'

    function.ui.plainTextEdit.setPlainText(out)


def tester(protocol):
    '''
    if protocol == 'all':
        proxy_list = {}
        for x in proto_list:
            proxy = get_proxy(x)
            proxy_list[x] = only_proxy(proxy)
    else:
        proxy_list = only_proxy(get_proxy(protocol))'''
    proxy_list = only_proxy(get_proxy(protocol))
    start_thread(proxy_list, protocol)
    viwe(work_proxy)

    '''while True:
        if threading.active_count() < 2:
            print(work_proxy)
            break
        time.sleep(0.1)'''

    '''elif protocol == 'http':
        pass
    elif protocol == 'https':
        pass
    elif protocol == 'socks4':
        pass
    elif protocol == 'socks5':
        pass'''
