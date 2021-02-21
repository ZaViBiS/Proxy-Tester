Proxy-Tester

Установка зависимостей:
pip install -r requirements.txt

## Использование:
```python main.py 3```

```←[Krunning threads |██████████                      | 516/1684
1684 threads were successfully launched

480 out of 1684 turned out to be workers and were recorded in the file

[Finished in 161.1s]```

В значение при запуске можно ввести название протокола или номер в списке
список :
* http       [1]
* https      [2]
* socks4     [3]
* socks5     [4] 


По окончанию в файле 'done.txt' будут рабочие proxy
* Удалите файл done.txt т.к. при повторном запусе программа просто начнет дописывать в конец файла

Доступные значения protocol:
* http, https, socks4, socks5

