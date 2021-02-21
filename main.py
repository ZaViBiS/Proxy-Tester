import sys

sys.path.append('source')  # Добовление дерикторию импорта

import time
import colorama
import threading
import functions
from cfg import *
from requests import get
from progress.bar import ShadyBar


# --- Инициализация colorama'ы --- #
colorama.init()


# --- Выбор протокола proxy --- #
# Если значение при запуске не было передано
if len(sys.argv) <= 1:
    try:
        protocol = proticol_list[int(input(open_text)) - 1]
 
    except Exception as e:
        print('Что-то не так')
        print('----- (｡•́︿•̀｡) -----')
        print(e)

        # Завиршение
        quit()

# Если было
else:
    try:
        protocol = proticol_list[int(sys.argv[1]) - 1]
    except:
        # Проверка на правильность написания
        for x in proticol_list:
            if x == str(sys.argv[1]):
                protocol = x
                break

        # Если протокол не указан - завиршение
        if protocol == '':
            print('(｡•́︿•̀｡)')
            quit()



# --- Начала замера выполнения --- #
start = time.time()

# --- Получение списка ip адресов и добавление в список --- #
for x in get(url + protocol).text:
    if x == '\n':
        proxy_list.append(for_for)
        for_for = ''
    else:
        for_for += x

# -^ Удаление из списка: '\n' ^- #
proxy_list = [line.rstrip() for line in proxy_list]

# линия загрузки
bar = ShadyBar('running threads', max=len(proxy_list))

# --- Запуск потоков для проверки proxy --- #
for x in range(len(proxy_list)):
    threading.Thread(target=functions.apoi, args=(str(proxy_list[x]), protocol)).start()
    bar.next()


print(colorama.Style.BRIGHT)

# Количество потоков
print(colorama.Fore.YELLOW + str(x) + colorama.Style.RESET_ALL +
      ' threads were successfully launched')

# Количество секунд затраченое на выполнение 
while len(threading.enumerate()) != 1:
    time.sleep(0.1)
    
# --- запись рабочих адресов в файл --- #
functions.writa()

print(colorama.Style.BRIGHT)
print('[Finished in ' + colorama.Fore.CYAN +
      str(round(time.time() - start, 2)) + colorama.Style.RESET_ALL + 's]')
