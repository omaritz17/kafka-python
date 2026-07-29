import logging.config
from typing import Any
from pathlib import Path

#LOG FILE PATH AND NAME

LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters":{
        "standard": {
        "format" : "%(asctime)s - %(levelname)s: %(name)s - %(message)s", # Structure of the log string
        "datefmt": "%Y-%m-%d %H:%M:%S",                         # Format for the %(asctime)s timestamp
        "style": "%",                                           # String formatting style ('%', '{', or '$')
        "validate": True,                                       # Validates format string on initialization
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level" : "INFO",
            "formatter": "standard",
            "filename": LOG_FILE,
            "encoding": "utf-8"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}

logging.config.dictConfig(LOGGING_CONFIG)