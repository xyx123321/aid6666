from socket import *
from threading import Thread
import sys

ADDR=('0.0.0.0',8888)
s=socket()
s.bind(ADDR)
s.listen(3)


def handle(c):
    while True:
        data=c.recv(1024).deconde()
        if not data:
            break
        print(data)
        c.sent(b'OK')
    c.close()



while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('...')
    except Exception as e:
        print(e)
        continue
    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()



