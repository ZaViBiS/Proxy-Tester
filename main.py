import sys

sys.path.append('source') # Добовление дерикторию импорта

import colorama
import threading
from cfg import *
from requests import get
from functions import apoi


# --- Инициализация colorama'ы --- #
colorama.init()

# --- Выбор протокола proxy --- #
if len(sys.argv) <= 1:
    protocol = 'http'
else:
    protocol = str(sys.argv[1])

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


print(colorama.Fore.CYAN + str(x) + colorama.Style.RESET_ALL + ' threads were successfully launched')