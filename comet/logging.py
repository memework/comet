import logging
import sys
from logging import Formatter, StreamHandler, INFO, DEBUG


class LoggingClass:
    def __init__(self, *args, **kwargs):
        self.log = logging.getLogger(__name__)


def setup_logging():
    root_logger = logging.getLogger()

    # Set levels.
    root_logger.setLevel(INFO)
    logging.getLogger('comet').setLevel(DEBUG)

    # Setup a good formatter. Copied from RoboDanny.
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', dt_fmt, style='{')

    # Print out log messages to stdout.
    stream = StreamHandler(stream=sys.stdout)
    stream.setFormatter(formatter)

    root_logger.addHandler(stream)
