from dataclasses import dataclass
import math
import sys

sys.path.insert(1, 'protos/python/PATH')
import rec_pb2


@dataclass
class Rec:
    name: str = "John"
    price: int = 99
    
    def discount(self, pc: int = 10):
        self.price = math.ceil(self.price * (100 - pc)/100)

if __name__ == "__main__":
    j = Rec()
    print(j)
    r = Rec("Long", 100)
    print(r)
    r.discount()
    print(r)
    r.discount()
    print(r)
    r.discount()
    print(r)
    r.discount()
    print(r)
    pb = rec_pb2.Rec()
    pb.name = "jjj"
    pb.price = 999
    print(pb.SerializeToString())
    pb2 = rec_pb2.Rec()
    pb2.ParseFromString(pb.SerializeToString())
    print(pb2)

