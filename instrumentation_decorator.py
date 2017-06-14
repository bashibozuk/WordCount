import datetime


def instrument(func):
    def new_func(*args, **kwargs):
        start = datetime.datetime.now()
        print('Starting execution of %s' % func.__name__)
        result = func(*args, **kwargs)
        time = datetime.datetime.now() - start
        print("The execution of %s took %d,%d seconds" % (func.__name__, time.seconds, time.microseconds))

        return result

    return new_func