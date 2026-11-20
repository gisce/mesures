import inspect
import pandas as pd

def check_line_terminator_param():
    if hasattr(inspect, 'signature'):
        params = inspect.signature(pd.DataFrame.to_csv).parameters
    else:
        params = inspect.getargspec(pd.DataFrame.to_csv).args

    if 'line_terminator' in params:
        return 'line_terminator'
    return 'lineterminator'

def to_csv_compat(dataf, file_path, **kwargs):
    param = check_line_terminator_param()
    separator = kwargs.get('sep', ',')
    terminator = kwargs.get(param)

    if terminator in (separator + '\n', separator + '\r\n'):
        dataf = dataf.copy()
        dataf.insert(len(dataf.columns), '__terminator__', '')
        kwargs[param] = terminator[1:]

    return dataf.to_csv(file_path, **kwargs)
