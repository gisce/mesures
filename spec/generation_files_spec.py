# -*- coding: utf-8 -*-
from mamba import description, it
from mesures.a5d import A5D
from mesures.agrecl import AGRECL
from mesures.almacenacau import ALMACENACAU
from mesures.autoconsumo import AUTOCONSUMO
from mesures.b5d import B5D
from mesures.cilcau import CILCAU
from mesures.cumpelectro import CUMPELECTRO
from mesures.cupselectro import CUPSELECTRO
from mesures.cupscau import CUPSCAU
from mesures.dates import *
from mesures.enelectroaut import ENELECTROAUT
from mesures.f1 import F1
from mesures.f3 import F3
from mesures.f5d import F5D
from mesures.mcil345 import MCIL345
from mesures.medidas import MEDIDAS
from mesures.p1 import P1
from mesures.p1d import P1D
from mesures.potelectro import POTELECTRO
from random import randint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
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

    @staticmethod
    def get_sample_f3_data():
        basic_f3 = {
            "cups": "ES00123400220F",
            "timestamp": "2020-01-01 00:00:00",
            "season": 1,
            "method": 1,
            "firmeza": 1
        }

        ts = "2020-01-01 00:00:00"
        data_f3 = []
        for x in range(50):
            datas = basic_f3.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae})
            data_f3.append(datas)

        cups = "ES00123400230F"
        ts = "2020-01-01 00:00:00"
        for x in range(70):
            datas = basic_f3.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'cups': cups})
            data_f3.append(datas)

        return data_f3

    @staticmethod
    def get_sample_cumpelectro_data():
        return [{
            'cups': 'ES00123400230F4444440F',
            'cif_empresa': 'X12345678',
            'codigo_solicitud': 'ABCDEFGHIJKLMNOPQRSTUVWXY',
            'version_solicitud': '123456',
            'electrointensivo_n1': 'S',
            'electrointensivo_n2': 'S',
            'electrointensivo_n3': 'S',
            'contrato_vigente_n1': 'S',
            'contrato_vigente_n2': 'S',
            'contrato_vigente_n3': 'S',
            'corriente_pagos_n1': 'N',
            'corriente_pagos_n2': 'S',
            'corriente_pagos_n3': 'S',
            'cargos_facturados_n1_p1': 100.0,
            'cargos_facturados_n1_p2': 100.0,
            'cargos_facturados_n1_p3': 100.0,
            'cargos_facturados_n1_p4': 100.0,
            'cargos_facturados_n1_p5': 100.0,
            'cargos_facturados_n1_p6': 100.0,
            'cargos_facturados_n2_p1': 100.0,
            'cargos_facturados_n2_p2': 100.0,
            'cargos_facturados_n2_p3': 100.0,
            'cargos_facturados_n2_p4': 100.0,
            'cargos_facturados_n2_p5': 100.0,
            'cargos_facturados_n2_p6': 100.0,
            'cargos_facturados_n3_p1': 100.0,
            'cargos_facturados_n3_p2': 100.0,
            'cargos_facturados_n3_p3': 100.0,
            'cargos_facturados_n3_p4': 100.0,
            'cargos_facturados_n3_p5': 100.0,
            'cargos_facturados_n3_p6': 100.0,
            'peajes_facturados_n1_p1': 100.0,
            'peajes_facturados_n1_p2': 100.0,
            'peajes_facturados_n1_p3': 100.0,
            'peajes_facturados_n1_p4': 100.0,
            'peajes_facturados_n1_p5': 100.0,
            'peajes_facturados_n1_p6': 100.0,
            'peajes_facturados_n2_p1': 100.0,
            'peajes_facturados_n2_p2': 100.0,
            'peajes_facturados_n2_p3': 100.0,
            'peajes_facturados_n2_p4': 100.0,
            'peajes_facturados_n2_p5': 100.0,
            'peajes_facturados_n2_p6': 100.0,
            'peajes_facturados_n3_p1': 100.0,
            'peajes_facturados_n3_p2': 100.0,
            'peajes_facturados_n3_p3': 100.0,
            'peajes_facturados_n3_p4': 100.0,
            'peajes_facturados_n3_p5': 100.0,
            'peajes_facturados_n3_p6': 100.0
        }]

    @staticmethod
    def get_sample_cupselectro_data():
        return [{
            'cups': 'ES00123400230F4444440F',
            'cif_empresa': 'X12345678',
            'codigo_solicitud': 'ABCDEFGHIJKLMNOPQRSTUVWXY',
            'version_solicitud': '123456',
            'fecha': '20220530',
            'requiere_f3': 'N',
            'nuevo_suministro': 'N'
        }]

    @staticmethod
    def get_sample_potelectro_data():
        return [{
            'cups': 'ES00123400230F4444440F',
            'cif_empresa': 'X12345678',
            'codigo_solicitud': 'ABCDEFGHIJKLMNOPQRSTUVWXY',
            'version_solicitud': '123456',
            'potencia_n-1_p1': 451.0,
            'potencia_n-1_p2': 451.0,
            'potencia_n-1_p3': 451.0,
            'potencia_n-1_p4': 451.0,
            'potencia_n-1_p5': 451.0,
            'potencia_n-1_p6': 451.0,
            'potencia_n-2_p1': 451.0,
            'potencia_n-2_p2': 451.0,
            'potencia_n-2_p3': 451.0,
            'potencia_n-2_p4': 451.0,
            'potencia_n-2_p5': 451.0,
            'potencia_n-2_p6': 451.0,
            'potencia_n-3_p1': 451.0,
            'potencia_n-3_p2': 451.0,
            'potencia_n-3_p3': 451.0,
            'potencia_n-3_p4': 451.0,
            'potencia_n-3_p5': 451.0,
            'potencia_n-3_p6': 451.0,
            'potencia_proyectada_p1': 451.0,
            'potencia_proyectada_p2': 451.0,
            'potencia_proyectada_p3': 451.0,
            'potencia_proyectada_p4': 451.0,
            'potencia_proyectada_p5': 451.0,
            'potencia_proyectada_p6': 451.0,
            'energia_proyectada_p1': 451.0,
            'energia_proyectada_p2': 451.0,
            'energia_proyectada_p3': 451.0,
            'energia_proyectada_p4': 451.0,
            'energia_proyectada_p5': 451.0,
            'energia_proyectada_p6': 451.0
        }]

    @staticmethod
    def get_sample_enelectroaut_data():
        return [{
            'cups': 'ES00123400230F4444440F',
            'cif_empresa': 'X12345678',
            'codigo_solicitud': 'ABCDEFGHIJKLMNOPQRSTUVWXY',
            'version_solicitud': '123456',
            'energia_n-1_p1': 10.0,
            'energia_n-1_p2': 10.0,
            'energia_n-1_p3': 10.0,
            'energia_n-1_p4': 10.0,
            'energia_n-1_p5': 10.0,
            'energia_n-1_p6': 10.0,
            'energia_n-2_p1': 10.0,
            'energia_n-2_p2': 10.0,
            'energia_n-2_p3': 10.0,
            'energia_n-2_p4': 10.0,
            'energia_n-2_p5': 10.0,
            'energia_n-2_p6': 10.0,
            'energia_n-3_p1': 10.0,
            'energia_n-3_p2': 10.0,
            'energia_n-3_p3': 10.0,
            'energia_n-3_p4': 10.0,
            'energia_n-3_p5': 10.0,
            'energia_n-3_p6': 10.0,
            'autoconsumida_proyectada_p1': 10.0,
            'autoconsumida_proyectada_p2': 10.0,
            'autoconsumida_proyectada_p3': 10.0,
            'autoconsumida_proyectada_p4': 10.0,
            'autoconsumida_proyectada_p5': 10.0,
            'autoconsumida_proyectada_p6': 10.0
        }]

    @staticmethod
    def get_sample_mcil345_data():
        return [{
            'cil': 'ES0291000000004444QR1F001',
            'timestamp': '2022-09-01 01:00:00',
            'season': 1,
            'ae': 100,
            'ai': 10,
            'r1': 1,
            'r2': 2,
            'r3': 3,
            'r4': 4,
            'read_type': 'R'
        },
            {
            'cil': 'ES0291000000005555QR1F001',
            'timestamp': '2022-09-01 01:00:00',
            'season': 1,
            'ae': 200,
            'ai': 20,
            'r1': 11,
            'r2': 22,
            'r3': 33,
            'r4': 44,
            'read_type': 'R'
            }]

    @staticmethod
    def get_sample_medidas_data():
        return [{
            'cil': 'ES0291000000004444QR1F001',
            'timestamp': '2022-09-01 01:00:00',
            'season': 1,
            'ae': 10,
            'r2': 2,
            'r3': 3,
            'power_factor': 0.55,
            'power_factor_type': 0,
            'read_type': 'R'
        },
            {
            'cil': 'ES0291000000005555QR1F001',
            'timestamp': '2022-09-01 01:00:00',
            'season': 1,
            'ae': 20,
            'r2': 2,
            'r3': 3,
            'power_factor': 0.55,
            'power_factor_type': 0,
            'read_type': 'R'
        }]


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


with description('An AGRECL'):
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

with description('An ALMACENACAU'):
    with it('with compression=False must be a raw file'):
        data = [
            {'cau': 'A', 'potencia_nominal': '1', 'energia_emmagatzemable': '12345', 'tecnologia_emmagatzematge': '1111',
             'data_alta': '2021-01-12', 'comentari': 'E0'}
        ]
        f = ALMACENACAU(data, compression=False)
        assert f.filename.endswith('.0')
        filepath = f.writer()
        assert 'bz2' not in filepath

with description('An AUTOCONSUMO'):
    with it('with compression=False must be a raw file'):
        data = [
            {'cau': 'A', 'miteco': '1', 'reg_auto_prov': '12345', 'reg_auto_def': '1111',
             'tipus_autoconsum': 'A', 'tipus_antiabocament': '1', 'nom': 'test', 'configuracio_mesura': '1111',
             'potencia_nominal': '2', 'codi_postal': '17007', 'subgrup': '12345', 'emmagatzematge': '1111',
             'data_alta': '2021-01-12'}
        ]
        f = AUTOCONSUMO(data, compression=False)
        assert f.filename.endswith('.0')
        filepath = f.writer()
        assert 'bz2' not in filepath

with description('An CUPSCAU'):
    with it('with compression=False must be a raw file'):
        data = [
            {'cau': 'A', 'cups': '1', 'tipus_consum': '12345', 'data_alta': '2021-01-12', 'comentari': 'E0'}
        ]
        f = CUPSCAU(data, compression=False)
        assert f.filename.endswith('.0')
        filepath = f.writer()
        assert 'bz2' not in filepath

with description('An CILCAU'):
    with it('with compression=False must be a raw file'):
        data = [
            {'cau': 'A', 'cil': '1', 'data_alta': '2021-01-12', 'comentari': 'E0'}
        ]
        f = CILCAU(data, compression=False)
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

with description('An F3'):
    with it('is instance of F3 Class'):
        data = SampleData().get_sample_f3_data()
        f = F3(data)
        assert isinstance(f, F3)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_f3_data()
        f = F3(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_f3_data()
        f = F3(data)
        res = f.writer()
        assert isinstance(f.ai, (int, np.int64))
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)


with description('A CUMPELECTRO'):
    with it('is instance of Cumpelectro Class'):
        data = SampleData().get_sample_cumpelectro_data()
        f = CUMPELECTRO(data)
        assert isinstance(f, CUMPELECTRO)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_cumpelectro_data()
        f = CUMPELECTRO(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_cumpelectro_data()
        f = CUMPELECTRO(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)


with description('A CUPSELECTRO'):
    with it('is instance of CUPSELECTRO Class'):
        data = SampleData().get_sample_cupselectro_data()
        f = CUPSELECTRO(data)
        assert isinstance(f, CUPSELECTRO)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_cupselectro_data()
        f = CUPSELECTRO(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_cupselectro_data()
        f = CUPSELECTRO(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

with description('A POTELECTRO'):
    with it('is instance of POTELECTRO Class'):
        data = SampleData().get_sample_potelectro_data()
        f = POTELECTRO(data)
        assert isinstance(f, POTELECTRO)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_potelectro_data()
        f = POTELECTRO(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_potelectro_data()
        f = POTELECTRO(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

with description('A ENELECTROAUT'):
    with it('is instance of ENELECTROAUT Class'):
        data = SampleData().get_sample_enelectroaut_data()
        f = ENELECTROAUT(data)
        assert isinstance(f, ENELECTROAUT)

    with it('a zip of raw Files'):
        data = SampleData().get_sample_enelectroaut_data()
        f = ENELECTROAUT(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_enelectroaut_data()
        f = ENELECTROAUT(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

with description('A MEDIDAS'):
    with it('is instance of MEDIDAS Class'):
        data = SampleData().get_sample_medidas_data()
        f = MEDIDAS(data)
        assert isinstance(f, MEDIDAS)

    with it('has its class methods'):
        data = SampleData().get_sample_medidas_data()
        f = MEDIDAS(data, period=2)
        res = f.writer()
        assert isinstance(f.cils, list)
        assert isinstance(f.number_of_cils, int)
        assert isinstance(f.ae, int)
        assert isinstance(f.r2, int)
        assert isinstance(f.r3, int)

with description('A MCIL345'):
    with it('is instance of MCIL345 Class'):
        data = SampleData().get_sample_mcil345_data()
        f = MCIL345(data)
        assert isinstance(f, MCIL345)

    with it('has its class methods'):
        data = SampleData().get_sample_mcil345_data()
        f = MCIL345(data)
        res = f.writer()
        assert isinstance(f.cils, list)
        assert isinstance(f.number_of_cils, int)
        assert isinstance(f.ae, int)
        assert isinstance(f.ai, int)
        assert isinstance(f.r1, int)
        assert isinstance(f.r2, int)
        assert isinstance(f.r3, int)
        assert isinstance(f.r4, int)

    with it('has its expected content'):
        data = SampleData().get_sample_mcil345_data()
        f = MCIL345(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F001;2022/09/01 01;1;100;10;1;2;3;4;R\n' \
                   'ES0291000000005555QR1F001;2022/09/01 01;1;200;20;11;22;33;44;R\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected
