import logging
import sys

#creater logger
logger = logging.getLogger(__name__)

#create formatter
formatter = logging.Formatter(fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#create handlers
stream_handler = logging.StreamHandler(stream = sys.stdout)
file_handler = logging.FileHandler('app.log')


#sets format
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]


#set log-level
logger.setLevel(logging.INFO)