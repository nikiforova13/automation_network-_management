import logging
import json
from datetime import datetime

logger = logging.getLogger()

logHandler = logging.StreamHandler()


class CustomJsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "level": record.levelname.upper(),
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
        }
        return json.dumps(log_record)


formatter = CustomJsonFormatter()

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
