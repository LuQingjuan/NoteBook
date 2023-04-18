import time
import random
from multiprocessing import Process


class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s piaoing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)

if __name__ == '__main__':
    p1=Piao('egon')
    p2=Piao('alex')
    p3=Piao('wupeiqi')
    p4=Piao('yuanhao')

    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')