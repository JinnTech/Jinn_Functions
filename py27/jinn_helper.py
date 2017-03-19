"""
This is the "jinn_helper" module.

The Jinn Helper module supplies many helper functions for python. 

"""
def progress(count, total, suffix=''):
    """
    Description: Outputs a progress bar at bottom of terminal. Slightly
    Usage: progress(iteration, total)
    Credits: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    Example:

    import time 

    total = 1000
    i = 0
    while i < total:
        progress(i, total)
        time.sleep(0.5)  # emulating long-playing job
        i += 1
    """
    import sys
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

