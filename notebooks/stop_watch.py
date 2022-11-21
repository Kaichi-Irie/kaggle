import time

from logs_func import create_logger, get_logger


## time_keeper.py
def stop_watch(VERSION):
    def _stop_watch(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            start = time.time()

            result = func(*args, **kargs)

            elapsed_time = int(time.time() - start)
            minites, sec = divmod(elapsed_time, 60)
            hour, minites = divmod(minites, 60)

            get_logger(VERSION).info(
                "[elapsed_time]\t>> {:0>2}:{:0>2}:{:0>2}".format(
                    hour, minites, sec
                )
            )

        return wrapper

    return _stop_watch
