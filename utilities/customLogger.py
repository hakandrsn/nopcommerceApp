import logging


class LogGen:
    @staticmethod
    def loggen():
        #  filemode a or w a = son kalınan yerden tutmaya başlar, w = baştan yazmaya başlar

        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s:%(levelname)s:%(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p:",
                            # filemode="a"
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
