import inspect
import pandas as pd

def check_line_terminator_param():
    # 'line_terminator' is deprecated in pandas
    # 'getargspec' is deprecated in python3
    if not hasattr(inspect, 'getargspec'):
        inspect.getargspec = inspect.getfullargspec
    params = inspect.getargspec(pd.DataFrame.to_csv).args
    if 'line_terminator' in params:
        return 'line_terminator'
    else:
        return 'lineterminator'