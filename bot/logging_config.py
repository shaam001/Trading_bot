import logging
import sys

def setup_logging():
    """Configures logging to file and console."""
    # how to write the log - time, name, level, message
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # File Handler
    file_handler = logging.FileHandler("trading_bot.log")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    # Console Handler: It will print logs to console else it will be only in the file
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger