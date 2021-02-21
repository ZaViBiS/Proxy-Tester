# --- Переменные --- #
proxy_list = []
url = 'https://www.proxy-list.download/api/v1/get?type='
for_for = ''
proticol_list = ['http', 'https', 'socks4', 'socks5']
protocol = ''

# --- Text --- #
open_text = '''
http       [1]
https      [2]
socks4     [3]
socks5     [4] 
           :'''
