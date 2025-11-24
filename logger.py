from logging.config import dictConfig
import logging

dictConfig(
    {
        "version": 1,
        "formatters": {
            "json": {
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "logs/app.log",  # this is where to store loggs in file
                "formatter": "json",  # this is the formate of logging
            },
            "console": {"class": "logging.StreamHandler", "formatter": "json"},
        },
        "root": {"level": "INFO", "handlers": ["console", "file"]},
    }
)

logger = logging.getLogger("Agent-run-log")