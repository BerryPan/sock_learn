import socket
import selectors
import random

sel = selectors.DefaultSelector()


def write(sock):
    sock.send(str(random.randint(0, 99)).encode('utf-8'))  # 发送必须是一个byts的数据,需要转码
    sel.unregister(sock)  # 当发送成功后必须取消注册,用与接下来的接收(读)到数据的注册
    sel.register(sock, selectors.EVENT_READ, read)  # 注册一个读的事件


def read(sock):
    data = sock.recv(1024)
    if not data:  # 判断接收到的数据是否为空数据
        sel.unregister(sock)  # 当接收完成后,依然是取消注册
        sock.close()  # 到此和服务器的请求基本处理完成,关闭套接字
        return
    print('receiver server %s' % data)


for i in range(100):  # 开1000个客户端测试
    client = socket.socket()
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 防止编辑器的每次运行端口冲突问题
    client.connect(('101.132.135.198', 1234))
    sel.register(client, selectors.EVENT_WRITE, write)  # 注册一个写的事件,接下来处理发送(写)事件的处理

while True:
    all_event = sel.select()
    print(all_event)
    for event, mask in all_event:
        sock = event.fileobj
        callback = event.data  # 创建一个回调函数,方便触发事务执行
        callback(sock)  # 调用刚创建的回调函数
