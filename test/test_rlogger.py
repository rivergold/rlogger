import sys
sys.path.append('..')
from rlogger import RLogger

if __name__ == '__main__':
    RLogger.init('./test.log', level='ERROR')
    RLogger.log('info', RLogger.INFO)
    RLogger.log('warning', RLogger.WARNING)
    RLogger.log('error', RLogger.ERROR)
