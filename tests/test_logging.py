import sys
import os
import logging
import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_config import setup_logging

# Setup logging for tests
setup_logging()

def test_logging_info(caplog):
    with caplog.at_level(logging.INFO):
        logger = logging.getLogger('my_logger')
        logger.info("This is an info message.")
    
    assert "This is an info message." in caplog.text

def test_logging_debug(caplog):
    with caplog.at_level(logging.DEBUG):
        logger = logging.getLogger('my_logger')
        logger.debug("This is a debug message.")
    
    assert "This is a debug message." in caplog.text
