#!/usr/bin/env python3
"""
A simple, append-only log file writer.
No external dependencies. No database. Just lines in a file.
Usage: from simple_logger import log
"""
import os
import datetime

class SimpleLogger:
    def __init__(self, log_dir="/config/byron/logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    @property
    def log_file(self):
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.log_dir, f"{date_str}.log")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(line)

# Initialize global instance
logger = SimpleLogger()

def log(message):
    logger.log(message)
