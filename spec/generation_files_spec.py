# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from expects import expect, equal
from mamba import context, description, it
from mesures.f1 import F1
from mesures.f5d import F5D
from mesures.p1 import P1
from mesures.p1d import P1D
from random import randint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import base64
import bz2
import numpy as np



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
        import zipfile
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_data()
        f = F1(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))
        assert f.ai == f.total
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)


with description('An P1'):
    with it('instance of P1 Class'):
        data = SampleData().get_sample_data()
        f = P1(data)
        assert isinstance(f, P1)

with description('An P1D'):
    with it('instance of P1D Class'):
        data = SampleData().get_sample_data()
        f = P1D(data)
        assert isinstance(f, P1D)