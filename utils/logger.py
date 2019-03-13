import os
import logging.config
import yaml

# logger.setLevel(level = logging.DEBUG)
# current_path = os.path.split(os.path.realpath(__file__))[0]
# log_path = current_path + '/../report/log.txt'
# handler = logging.FileHandler(log_path)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
# handler.setFormatter(formatter)
#
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
#
# logger.addHandler(handler)
# logger.addHandler(console)
#
# logger.info("nihao")
# logger.error("nihao2")

log_path = os.path.split(os.path.realpath(__file__))[0] + '/../conf/logger_config.yaml'

def setup_logging(default_path = log_path,default_level = logging.INFO):
    print(log_path)
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

logger = logging.getLogger('info')
logger.error('Faild to get result', exc_info=True)
setup_logging()
# try:
#     result = 10 / 0
# except Exception:
#     logger.error('Faild to get result', exc_info=True)
# logger.info('Finished')
# logger.error('Finished')