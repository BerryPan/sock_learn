import socket
import selectors
from serverToClient_pb2 import *
from clientToServer_pb2 import *
import random
result = []


class Server(object):

    def __init__(self, sel, sock):
        self.sel = sel
        self.sock = sock

    def run(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(50)
        self.sock.setblocking(False)  # 设置非阻塞
        self.sel.register(sock, selectors.EVENT_READ, self.accept)
        while True:
            events = self.sel.select()  # 默认是阻塞，有活动连接就返回活动连接列表
            for key, mask in events:
                callback = key.data  # 创建一个回调函数并获取
                callback(key.fileobj, mask)  # 调用回调函数

    def accept(self, sock, mask):
        conn, addr = sock.accept()  # 已经就绪，等待接收
        print('连接来自于{0}'.format(addr))
        conn.setblocking(False)
        # sock.send(str('thanks').decode())
        sel.register(conn, selectors.EVENT_READ, self.read)  # 注册事件

    def read(self, conn, mask):
        data = conn.recv(1024)  # 就绪，等待接收数据
        if data:  # 判断是否有数据过来，有就执行

            local = Local()
            try:
                local.ParseFromString(data)
            except:
                True

            print('来自客户端：', local)

            another = Another()
            another.pos_x = random.uniform(-100, 100)
            another.pos_y = random.uniform(-100, 100)
            another.pos_z = random.uniform(-100, 100)
            another.rot_x = random.uniform(-100, 100)
            another.rot_y = random.uniform(-100, 100)
            another.rot_z = random.uniform(-100, 100)
            data = another.SerializeToString()

            conn.send(data)
        else:
            print('准备关闭连接', conn)
            sel.unregister(conn)
            conn.close()


if __name__ == '__main__':
    sel = selectors.DefaultSelector()  # 默认的选择方式
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host, port = '127.0.0.1', 1234
    server_obj = Server(sel, sock)
    server_obj.run(host, port)
