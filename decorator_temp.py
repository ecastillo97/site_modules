
from functools import wraps

def decorator_name(func):
    @wraps(func)
    def weapper(*args, **kwargs):
        # code to exec before calling the decorated function/.
        #call decorated function as required, returning its results if needed.
        # code to exec instead of calling the decorated function

        return wrapper
