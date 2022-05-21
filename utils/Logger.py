import logging
from pathlib import Path


class Logger:

    ROOT_PATH = str(Path(__file__).parent.parent)

    def get_logger(self, test_name, class_name):
        loggerName = f"{class_name}_{test_name}"
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(self.ROOT_PATH + "/logs/" + f'{loggerName}.log', mode='w')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
