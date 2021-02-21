import threading
from cfg import *
from sys import argv
from functions import apoi
from requests import get


# --- Выбор протокола proxy --- #
if len(argv) <= 1:
    protocol = 'http'
else:
    protocol = str(argv[1])

# --- Получение списка ip адресов и добавление в список --- #
for x in get(url + protocol).text:
    if x == '\n':
        proxy_list.append(for_for)
        for_for = ''
    else:
        for_for += x

# -^ Удаление из списка: '\n' ^- #
proxy_list = [line.rstrip() for line in proxy_list]

# --- Запуск потоков для проверки proxy --- #
for x in range(len(proxy_list)):
    threading.Thread(target=apoi, args=(str(proxy_list[x]), protocol)).start()


print('{0} threads were successfully launched'.format(x))