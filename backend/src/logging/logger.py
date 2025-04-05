import os
from logging import config, getLogger


class MyLoggerConfig:
    def __init__(self):
        self.config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "simple": {
                    "format": "%(name)s %(asctime)s %(funcName)s [%(levelname)s]: %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": os.getenv("LOG_LEVEL", "DEBUG"),
                    "stream": "ext://sys.stdout",
                    "formatter": "simple",
                }
            },
            "root": {
                "level": os.getenv("LOG_LEVEL", "DEBUG"),
                "handlers": ["console"],
            },
        }

    def configure(self):
        try:
            config.dictConfig(self.config)
        except ValueError as e:
            print(f"Error configuring logger: {e}")


logger_config = MyLoggerConfig()
logger_config.configure()

logger = getLogger("backendlog")
