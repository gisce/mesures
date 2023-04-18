import inspect
import pandas as pd

def check_line_terminator_param():
    if 'line_terminator' in inspect.getargspec(pd.DataFrame.to_csv).args:
        return 'line_terminator'
    else:
        return 'lineterminator'