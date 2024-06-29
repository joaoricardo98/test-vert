import logging
import os
from datetime import datetime


class Logger(logging.Logger):
    def __init__(self, name) -> None:
        logging.Logger.__init__(self, name, logging.INFO)

        if not os.path.exists('logs'):
            os.makedirs('logs')

        now = datetime.now()
        log_name = f'{now.year}-{now.month}-{now.day}'
        fh = logging.FileHandler(filename=f'logs/{log_name}.log')
        sh = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s - %(levelname)s]  %(message)s')

        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.addHandler(sh)
        self.addHandler(fh)
