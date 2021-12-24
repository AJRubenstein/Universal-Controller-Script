"""
config.py

Stores any modified parts of the configuration for the script, allowing for
customisation of the script's behaviour. Any settings found here will override
those found in the default configuration.
"""

from .logger import verbosity

CONFIG = {
    "logger.max_verbosity": verbosity.CRITICAL
}
