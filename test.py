from requests import get
import threading
from saver import *
info = get('https://www.proxy-list.download/api/v1/get?type=http').text
l = []
done = ''
for x in info:
    if x == '\n':
        l.append(done)
        done = ''
    else:
        done += x

    
l = [line.rstrip() for line in l]
num = 0
for x in range(len(l)):
    s = threading.Thread(target=apoi, args=(str(l[num]), 'http')).start()
    num += 1
print(num)

# print({info['protocol'] : str(info['ip'] + ':' + info['port'])})