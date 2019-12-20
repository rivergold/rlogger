import logging
import traceback
import datetime


class RLogger(object):

    logger = logging.getLogger('logger')
    log_level = logging.INFO
    logger.setLevel(logging.DEBUG)

    log_file_handler = None
    log_stream_handler = None

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

    @classmethod
    def init(cls, log_file, screen_log=True, level='INFO'):

        if level == 'DEBUG':
            cls.set_level(cls.DEBUG)
        elif level == 'INFO':
            cls.set_level(cls.INFO)
        elif level == 'WARNING':
            cls.set_level(cls.WARNING)
        elif level == 'ERROR':
            cls.set_level(cls.ERROR)
        else:
            raise ValueError(
                'Not support log level: {}, only support DEBUG, WARNING and ERROR'
                .format(level))

        if cls.log_file_handler not in cls.logger.handlers:
            formatter = logging.Formatter(
                '%(name)s-%(levelname)s %(asctime)s: %(message)s')
            cls.log_file_handler = logging.FileHandler(log_file,
                                                       encoding='utf-8')
            cls.log_file_handler.setFormatter(formatter)
            cls.logger.addHandler(cls.log_file_handler)
        if screen_log is True:
            if cls.log_stream_handler not in cls.logger.handlers:
                cls.log_stream_handler = logging.StreamHandler()
                cls.log_stream_handler.setFormatter(formatter)
                cls.logger.addHandler(cls.log_stream_handler)
        cls.log(
            '***************************************************************************************',
            level=cls.INFO)
        cls.log(
            '******************** Program started at {} ********************'.
            format(datetime.datetime.now()))
        cls.log(
            '***************************************************************************************',
            level=cls.INFO)

    @classmethod
    def set_level(cls, level):
        cls.logger.setLevel(level)

    @classmethod
    def log(cls, message, level=None):
        name = traceback.extract_stack()[-2][0]
        cls.logger.name = name.split('/')[-1][:-3]
        if level is None:
            cls.logger.log(cls.INFO, message)
        else:
            cls.logger.log(level, message)

    @classmethod
    def close(cls):
        handlers = cls.logger.handlers[:]
        for handler in handlers:
            cls.logger.removeHandler(handler)
