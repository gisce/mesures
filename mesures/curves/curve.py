import pandas as pd

class DummyCurve(object):
    def __init__(self, datas):
        """
        Parse a curvedata
        :param datas:
        """
        if isinstance(datas, (list, tuple)):
            pass
        for data in datas:
            # Check lowers keys
            for k, v in data.items():
                data[k.lower()] = data.pop(k)
            # Adapt datetimes
            if 'datetime' in data:
                data['timestamp'] = data.pop('datetime')
            data['timestamp'] = pd.Timestamp(data['timestamp'])
            if 'estacio' in data:
                data['season'] = data.pop('estacio')
            if 'as' in data:
                # Active input and export
                data['ae'] = data.pop('as')
                data['ai'] = data.pop('ae')
            if 'season' in data and isinstance(data['season'], str):
                try:
                    data['season'] = int(data['season'])
                except ValueError:
                    # str season
                    data['season'] = 0 if data['season'].lower() == 'w' else 1
            for k in ('ai', 'ae', 'r1', 'r2', 'r3', 'r4'):
                if k not in data:
                    data[k] = 0
        self.curve_data = datas
