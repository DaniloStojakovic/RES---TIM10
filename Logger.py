import logging

# create logger
logger = logging.getLogger('logFile')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('logFile.txt')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


# 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warning('warn message')
#logger.error('error message')
#logger.critical('critical message')
#primjeri poziva loggera

#2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
#2005-03-19 15:10:26,620 - simple_example - INFO - info message
#2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
#2005-03-19 15:10:26,697 - simple_example - ERROR - error message
#2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
