import logging

logger = logging.getLogger('晨')
logger.setLevel(logging.ERROR)

A = logging.StreamHandler()
A.setLevel(logging.INFO)

B = logging.FileHandler('log.log')
B.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')


A.setFormatter(formatter)
B.setFormatter(formatter)
logger.addHandler(A)
logger.addHandler(B)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')




