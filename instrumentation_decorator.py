import datetime


def instrument(func):
    def new_func(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        time = datetime.datetime.now() - start
        print("The execution took %d,%d seconds" % (time.seconds, time.microseconds))

    return new_func