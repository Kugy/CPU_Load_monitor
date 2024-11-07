import psutil
import logging
from datetime import time
from logging.handlers import RotatingFileHandler

#Creating a log file and managing log file backup

log_file = 'cpu_load_monitor.log'
cpu_load_size = 2 * 1024 # 2 KB data size
backup_count = 5 # Backup of 5 old log files

logging.basicConfig(handlers = [RotatingFileHandler(log_file,
                              maxBytes = cpu_load_size,
                              backupCount = backup_count)],
                    level = logging.INFO,
                    format ='%(asctime)s - %(levelname)s - %(message)s')

print("So far the implementation is good, Jattebra")
