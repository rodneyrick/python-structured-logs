
# from loggers.logger import configure_logger
# import structlog

import loggers
import app

logger = loggers.configure_logger("main")

try:
    logger.info("e")
    app.f()
    1/0
except ZeroDivisionError:
    logger.exception("Cannot divide by zero!")
