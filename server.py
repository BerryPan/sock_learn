import socket
import selectors
from serverToClient_pb2 import *
from clientToServer_pb2 import *
import random
result = []
qsf = Another()
pjm = Another()
ljn = Another()


addr = ''


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
        conn.setblocking(False)
        # sock.send(str('thanks').decode())
        sel.register(conn, selectors.EVENT_READ, self.read)  # 注册事件

    def read(self, conn, mask):
        global pjm
        global qsf
        global ljn
        data = conn.recv(1024)  # 就绪，等待接收数据
        if data:  # 判断是否有数据过来，有就执行

            local = Local()
            try:
                local.ParseFromString(data)
                if local.name == 'qsf':
                    another = Another()
                    another.name = 'pjm'
                    another.pos_x = pjm.pos_x
                    another.pos_y = pjm.pos_y
                    another.pos_z = pjm.pos_z
                    another.rot_x = pjm.rot_x
                    another.rot_y = pjm.rot_y
                    another.rot_z = pjm.rot_z
                    another.hp = pjm.hp

                else:
                    another = Another()
                    another.name = 'qsf'
                    another.pos_x = qsf.pos_x
                    another.pos_y = qsf.pos_y
                    another.pos_z = qsf.pos_z
                    another.rot_x = qsf.rot_x
                    another.rot_y = qsf.rot_y
                    another.rot_z = qsf.rot_z
                    another.hp = qsf.hp
                data = another.SerializeToString()
                conn.send(data)
                print(local)
                if local.name == 'qsf':
                    qsf = local

                if local.name == 'pjm':
                    pjm = local

                if local.name == 'ljn':
                    ljn = local

            except:
                True


            sel.unregister(conn)
            conn.close()


if __name__ == '__main__':
    sel = selectors.DefaultSelector()  # 默认的选择方式
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host, port = '172.19.15.164', 1234
    server_obj = Server(sel, sock)
    server_obj.run(host, port)
