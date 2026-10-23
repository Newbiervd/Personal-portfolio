import os
import logging

def setup_logging(name):
    """Sets up a basic logger for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(name)

def ensure_directory_exists(directory_path):
    """Ensures that a directory exists; if not, creates it."""
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)
