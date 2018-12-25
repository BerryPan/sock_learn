from serverToClient_pb2 import *

result = []
d = {}

def write_test():
    p = Another()
    p.pos_x = 50
    p.pos_y = -50
    p.pos_z = -50
    p.rot_x = 50
    p.rot_y = -50
    p.rot_z = -50
    p.hp = 100
    d['asd'] = p


if __name__ == "__main__":
    write_test()
    print(d['asd'])
