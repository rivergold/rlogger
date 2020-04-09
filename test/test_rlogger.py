import sys
sys.path.append('.')
import multiprocessing
from rlogger import RLogger


def run():
    print('ok')
    RLogger.log('test')


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    RLogger.init('./test.log')

    p1 = multiprocessing.Process(target=run)
    p2 = multiprocessing.Process(target=run)

    p1.start()
    p2.start()
