import pandas as pd
import numpy as np

class DummyCurve(object):
    def __init__(self, datas):
        """
        Parse a curvedata format
        :param datas: list of dicts
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
            if 'local_datetime' in data:
                data['timestamp'] = data.pop('local_datetime')
            data['timestamp'] = pd.Timestamp(data['timestamp'])
            if 'estacio' in data:
                data['season'] = data.pop('estacio')
            if 'season' not in data:
                data['season'] = int(data['timestamp'].dst().seconds > 0)
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

class DummyKeys(object):
    def __init__(self, datas):
        """
        Parse fields
        Set dict names as basic key names
        Set dict lower keys
        :param datas: list of dicts
        """
        for data in datas:
            # Lower keys
            # Split separators in keys dict
            for k, v in data.items():
                data[k.lower()] = data.pop(k)
                try:
                    # Try to fix keynames with dots and agrees
                    data[k.split('.')[-1]] = data.pop(k)
                    data[k.split('agree_')[-1]] = data.pop(k)
                except:
                    continue
            if 'origin' in data:
                data['origen'] = data.pop('origin')
            if 'operation_type' in data:
                data['tipus_operacio'] = data.pop('operation_type')
            if 'data_inici' in data:
                data['data_alta'] = data.pop('data_inici')
            if 'data_final' in data:
                data['data_baixa'] = data.pop('data_final')
            if 'data_inici_ag' in data:
                data['data_alta'] = data.pop('data_inici_ag')
            if 'data_final_ag' in data:
                data['data_baixa'] = data.pop('data_final_ag')
            if 'data_alta' in data:
                data['data_alta'] = pd.Timestamp(data['data_alta'])
            if 'data_baixa' in data and data['data_baixa']:
                data['data_baixa'] = pd.Timestamp(data['data_baixa'])
            else:
                data['data_baixa'] = np.nan
        self.data = datas
