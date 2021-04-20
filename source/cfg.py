# --- Переменные --- #
proxy_list = []
url = 'https://www.proxy-list.download/api/v1/get?type='
for_for = ''
proticol_list = ['all', 'http', 'https', 'socks4', 'socks5']
protocol = ''
json_file = True # Если json_file = True будет создан дополнительный файл в формате json


# --- Text --- #
open_text = '''
all        [1]
http       [2]
https      [3]
socks4     [4]
socks5     [5] 
           :'''
