Proxy-Tester

Установка зависимостей:
pip install -r requirements.txt

Использование:
python main.py [protocol]
* Стандартный 'http' *

По окончанию в файле 'done.txt' будут рабочие proxy
* Удалите файл done.txt т.к. при повторном запусе программа просто начнет дописывать в конец файла *

Доступные значения protocol:
http, https, socks4, socks5
