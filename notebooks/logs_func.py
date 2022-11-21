
from functools import wraps
from logging import (
    DEBUG,
    INFO,
    FileHandler,
    Formatter,
    StreamHandler,
    getLogger,
)
from pathlib import Path

# from base_log import get_logger

## base_log.py
def create_logger(exp_version):
    log_file = Path(f"{exp_version}.log").resolve()

    # logger
    logger_ = getLogger(exp_version)
    logger_.setLevel(DEBUG)

    # formatter
    fmr = Formatter("[%(levelname)s] %(asctime)s >>\t%(message)s")

    # file handler
    fh = FileHandler(log_file)
    fh.setLevel(DEBUG)
    fh.setFormatter(fmr)

    # stream handler
    ch = StreamHandler()
    ch.setLevel(INFO)
    ch.setFormatter(fmr)

    logger_.addHandler(fh)
    logger_.addHandler(ch)


def get_logger(exp_version):
    return getLogger(exp_version)
