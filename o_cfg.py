# --- Переменные --- #
# proxy_list = []
url = 'https://www.proxy-list.download/api/v1/get?type='
heders = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
# for_for = ''
# proticol_list = ['all', 'http', 'https', 'socks4', 'socks5']
proto_list = ['http', 'https', 'socks4', 'socks5']
# protocol = ''
# json_file = False # Если json_file = True будет создан дополнительный файл в формате json
max_thread = 10000  # Максимальное количество потоков
sleep_time = 0.1  # Время ожидания между проверкой количества потоков


# --- Text --- #
open_text = '''
all        [1]
http       [2]
https      [3]
socks4     [4]
socks5     [5] 
           :'''
