# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from expects import expect, equal
from mamba import context, description, it
from mesures.f1 import F1
from mesures.f5d import F5D
from mesures.p1 import P1
from mesures.p1d import P1D
from mesures.a5d import A5D
from mesures.b5d import B5D
from mesures.agrecl import AGRECL
from random import randint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import base64
import bz2
import numpy as np
import zipfile


class SampleData:
    @staticmethod
    def get_sample_data():
        basic_f1 = {
            "cups": "ES00123400220F",
            "name": "50148869",
            "timestamp": "2020-01-01 00:00:00",
            "type": "p",
            "season": "W",
            "ae": 28290, "ai": 0,
            "r1": 0, "r2": 4880, "r3": 0, "r4": 0,
            "cch_bruta": True, "cch_fact": False,
            "ai_fact": 0, "ae_fact": 0,
            "r1_fact": 0, "r2_fact": 0, "r3_fact": 0, "r4_fact": 0,
            "quality_ai": 0, "quality_ae": 0,
            "quality_r1": 0, "quality_r2": 0, "quality_r3": 0, "quality_r4": 0,
            "quality_res": 0, "quality_res2": 0,
            "firm_fact": False,
        }

        ts = "2020-01-01 00:00:00"
        data_f1 = []
        for x in range(50):
            datas = basic_f1.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2})
            data_f1.append(datas)

        cups = "ES00123400230F"
        ts = "2020-01-01 00:00:00"
        for x in range(70):
            datas = basic_f1.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 10)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'cups': cups})
            data_f1.append(datas)

        return data_f1

    @staticmethod
    def get_sample_f5d_data():
        basic_f5d = {
            "cups": "ES00123400220F",
            "timestamp": "2020-01-01 00:00:00",
            "season": "W",
            "magn": 1,
            "ae": 0, "ai": 0,
            "r1": 0, "r2": 0, "r3": 0, "r4": 0,
            "cch_bruta": True, "cch_fact": False,
            "ai_fact": 0, "ae_fact": 0,
            "r1_fact": 0, "r2_fact": 0, "r3_fact": 0, "r4_fact": 0,
            "kind_fact": 1,
            "firm_fact": False,
            'invoice_number': 'FE20214444'
        }

        ts = "2020-01-01 00:00:00"
        data_f5d = []
        data_f5d_kwh = []
        for x in range(50):
            datas = basic_f5d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai_fact = randint(0, 5000)
            ae_fact = randint(0, 2)
            r1_fact = randint(0, 30)
            r2_fact = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai_fact': ai_fact, 'ae_fact': ae_fact,
                          'r1_fact': r1_fact, 'r2_fact': r2_fact})
            data_f5d.append(datas)

        cups = "ES00123400230F"
        ts = "2020-01-01 00:00:00"
        for x in range(70):
            datas = basic_f5d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai_fact = randint(0, 5000)
            ae_fact = randint(0, 2)
            r1_fact = randint(0, 30)
            r2_fact = randint(0, 10)
            datas.update({'timestamp': ts, 'ai_fact': ai_fact, 'ae_fact': ae_fact,
                          'r1_fact': r1_fact, 'r2_fact': r2_fact,
                          'cups': cups})
            data_f5d.append(datas)

        return data_f5d


with description('An F5D'):
    with it('is instance of F5D Class'):
        data = SampleData().get_sample_f5d_data()
        f = F5D(data)
        assert isinstance(f, F5D)

    with it('has its class methods'):
        data = SampleData().get_sample_f5d_data()
        f = F5D(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))


with description('An F1'):
    with it('is instance of F1 Class'):
        data = SampleData().get_sample_data()
        f = F1(data)
        assert isinstance(f, F1)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_data()
        f = F1(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_data()
        f = F1(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))
        assert f.ai == f.total
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)


with description('A AGRECL'):
    with it('with compression=False must be a raw file'):
        data = [
            {'origen': 'A', 'tipus_operacio': '', 'distribuidora': '12345', 'comercialitzadora': '1111',
             'tensio': 'E0', 'tarifa': '2T', 'dh': 'E3', 'tipo': '5', 'provincia': 'GI', 'tipus_demanda': '0',
             'data_alta': '2021-01-12'}
        ]
        f = AGRECL(data, compression=False)
        assert f.filename.endswith('.0')
        filepath = f.writer()
        assert 'bz2' not in filepath

with description('A P1'):
    with it('instance of P1 Class'):
        data = SampleData().get_sample_data()
        f = P1(data)
        assert isinstance(f, P1)

    with it('is a zip file'):
        data = SampleData().get_sample_data()
        f = P1(data, distributor='9999')
        filepath = f.writer()
        assert zipfile.is_zipfile(filepath)
        assert f.zip_filename.endswith('.zip')

    with it('with bz2 activated, must be a daily bz2 file in a zip'):
        data = SampleData().get_sample_data()
        f = P1(data, distributor='1234', compression='bz2')
        filepath = f.writer()
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        assert isinstance(filepath, str)
        assert '.bz2' not in filepath

        # Decompress ppal zip file and decompress bz2 files
        zip_file = zipfile.ZipFile(filepath, "r")
        for name in zip_file.namelist():
            assert name.endswith('.bz2')
            file_bz2 = bz2.decompress(zip_file.read(name))

with description('A P1D'):
    with it('instance of P1D Class'):
        data = SampleData().get_sample_data()
        f = P1D(data)
        assert isinstance(f, P1D)

    with it('bz2 as a default compression'):
        data = SampleData().get_sample_data()
        f = P1D(data)
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        f1 = f.writer()
        assert isinstance(f1, str)
        assert '.bz2' in f1

with description('An A5D'):
    with it('bz2 as a default compression'):
        f = A5D([{'cups': 'XDS', 'timestamp': datetime.now(), 'season': 1, 'ai': 0, 'factura': 123}], compression='bz2')
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        f1 = f.writer()
        assert f1.endswith('.bz2')

    with it('a raw file'):
        f = A5D([{'cups': 'XDS', 'timestamp': datetime.now(), 'season': 1, 'ai': 0, 'factura': 123}], compression=False)
        assert isinstance(f.filename, str)
        assert '.bz2' not in f.filename
        assert f.filename.endswith('.0')
        f1 = f.writer()
        assert isinstance(f1, str)
        assert 'bz2' not in f1
        assert f1.endswith('.0')

with description('A B5D'):
    with it('bz2 as a default compression'):
        f = B5D([{'cups': 'XDS', 'timestamp': datetime.now(), 'season': 1, 'ai': 0, 'factura': 123}],
                distributor='1234', comer='1235', compression='bz2')
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        f1 = f.writer()
        assert isinstance(f1, str)
        assert f1.endswith('.bz2')

    with it('a raw file'):
        f = B5D([{'cups': 'XDS', 'timestamp': datetime.now(), 'season': 1, 'ai': 0, 'factura': 123}], compression=False)
        assert isinstance(f.filename, str)
        assert '.bz2' not in f.filename
        assert f.filename.endswith('.0')
        f1 = f.writer()
        assert isinstance(f1, str)
        assert 'bz2' not in f1
        assert f1.endswith('.0')

