import logging
import socket
from logging.handlers import SysLogHandler


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


class Logger:
    def __init__(self, url, code, app_name, logging_level):
        syslog = SysLogHandler(address=(url, code))
        syslog.addFilter(ContextFilter())
        format = "%(asctime)s %(levelname)s from %(hostname)s " + app_name + " (%(process)d): %(message)s"
        formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
        syslog.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(syslog)
        logger.setLevel(logging_level)