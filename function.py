from PyQt5 import QtWidgets, uic
from proxy import *


app = QtWidgets.QApplication([])
ui = uic.loadUi('proxy.ui')

protocol = ''
json_active = False

'''
def func(): return ui.time.setText("asd")
def dis(): return ui.time.clear()


status = lambda text='text': ui.statusbar.showMessage(str('text'))
'''


# func = lambda : ui.listWidget.addItem(parser())

# ui.setButton.clicked.connect()
def all_func():
    global protocol
    protocol = 'all'
    print(protocol)


def http_func():
    global protocol
    protocol = 'http'


def https_func():
    global protocol
    protocol = 'https'


def socks4_func():
    global protocol
    protocol = 'socks4'


def socks5_func():
    global protocol
    protocol = 'socks5'


def box():
    global json_active
    if ui.json_box.checkState():
        json_active = True
    else:
        json_active = False


def start():
    if protocol != '':
        tester(protocol)




ui.all.clicked.connect(all_func)
ui.http.clicked.connect(http_func)
ui.https.clicked.connect(https_func)
ui.socks4.clicked.connect(socks4_func)
ui.socks5.clicked.connect(socks5_func)

# ui.json_box.clicked.connect(box)

ui.start.clicked.connect(start)
