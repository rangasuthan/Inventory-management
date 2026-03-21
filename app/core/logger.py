import logging
import sys

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

filehandler=logging.FileHandler('inventory.log')
filehandler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
filehandler.setFormatter(formatter)

consolehandler = logging.StreamHandler(sys.stdout)
consolehandler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
consolehandler.setFormatter(console_formatter)

if not logger.handlers:
    logger.addHandler(filehandler)
    logger.addHandler(consolehandler)