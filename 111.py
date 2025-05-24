import logging
logger = logging.getLogger("my_name")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s -%(filename)s:%(lineno)d'))

fh = logging.FileHandler(filename= 'log.txt',encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s -%(filename)s:%(lineno)d'))

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('这是debug级别的调试信息')
logger.info('这是info级别的调试信息')