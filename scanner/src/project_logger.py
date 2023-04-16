import os
import logging, sys
from config import SCANNER_DIR

class CustomFormatter(logging.Formatter):

    green = "\x1b[32m;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(pathname)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    
logger = logging.getLogger('scanner_logger')
c_handler = logging.StreamHandler(sys.stdout)
c_handler.setLevel(logging.DEBUG)

if os.path.exists(f'{SCANNER_DIR}/logs') == False:
    os.mkdir(f'{SCANNER_DIR}/logs')
with open(f'{SCANNER_DIR}/logs/scanner.logs', 'w') as f:
    pass

f_handler = logging.FileHandler(f'{SCANNER_DIR}/logs/scanner.logs')
f_handler.setLevel(logging.WARNING)

c_handler.setFormatter(CustomFormatter())
f_handler.setFormatter(CustomFormatter())

logger.addHandler(c_handler)
logger.addHandler(f_handler)
logging.basicConfig(level=logging.DEBUG, handlers=[logging.NullHandler()])