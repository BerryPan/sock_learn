from serverToClient_pb2 import *

result = []


def write_test():
    b = Boss()
    b.hp = 100
    b.attack = 1
    p = Player()
    p.pos_x = 50
    p.pos_y = -50
    p.pos_z = -50
    p.rot_x = 50
    p.rot_y = -50
    p.rot_z = -50
    p.hp = 100
    result.append(b)


if __name__ == "__main__":
    write_test()