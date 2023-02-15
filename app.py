
# import app
import loggers

logger = loggers.get_logger()

def f():
    try:
        logger.info("e")
    except ZeroDivisionError:
        logger.exception("Cannot divide by zero!")
