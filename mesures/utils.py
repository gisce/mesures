import inspect
import pandas as pd

def check_line_terminator_param():
    try:
        params = inspect.getargspec(pd.DataFrame.to_csv).args
    except ValueError:
        params = inspect.getfullargspec(pd.DataFrame.to_csv).args
    except AttributeError:
        params = inspect.getfullargspec(pd.DataFrame.to_csv).args
    if 'line_terminator' in params:
        return 'line_terminator'
    else:
        return 'lineterminator'