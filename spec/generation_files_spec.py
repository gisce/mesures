# -*- coding: utf-8 -*-
from mamba import description, it
from mesures.a5d import A5D
from mesures.agrecl import AGRECL
from mesures.almacenacau import ALMACENACAU
from mesures.autoconsumo import AUTOCONSUMO
from mesures.b5d import B5D
from mesures.cilcau import CILCAU
from mesures.cildat import CILDAT
from mesures.cumpelectro import CUMPELECTRO
from mesures.cupselectro import CUPSELECTRO
from mesures.cups45 import CUPS45
from mesures.cupscau import CUPSCAU
from mesures.cupsdat import CUPSDAT
from mesures.dates import *
from mesures.enelectroaut import ENELECTROAUT
from mesures.f1 import F1
from mesures.f1qh import F1QH
from mesures.f3 import F3
from mesures.f5d import F5D
from mesures.mcil345 import MCIL345
from mesures.mcil345qh import MCIL345QH
from mesures.medidas import MEDIDAS
from mesures.obagrecl import OBAGRECL
from mesures.obcups import OBCUPS
from mesures.p1 import P1
from mesures.p1d import P1D
from mesures.p2d import P2D
from mesures.p5d import P5D
from mesures.pmest import PMEST
from mesures.potelectro import POTELECTRO
from mesures.reobje2 import REOBJE2
from mesures.reobjecil import REOBJECIL
from mesures.reobjeagrecl import REOBJEAGRECL
from mesures.reobjeincl import REOBJEINCL
from random import randint
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import bz2
import numpy as np
import zipfile

DELETE_FILES = 'rm -rf *.bz2 *.zip *.[0123456789] medidas_*.txt'

class SampleData:
    @staticmethod
    def get_sample_data():
        basic_f1 = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2022-01-01 01:00:00",
            "tipo_medida": "p",
            "season": "W",
            "ae": 10,
            "ai": 10,
            "r1": 10,
            "r2": 10,
            "r3": 10,
            "r4": 10,
            "quality_ai": 0,
            "quality_ae": 0,
            "quality_r1": 0,
            "quality_r2": 0,
            "quality_r3": 0,
            "quality_r4": 0,
            "quality_res": 0,
            "quality_res2": 0,
            "method": 1,
        }

        data_f1 = [basic_f1.copy()]

        ts = "2022-01-01 01:00:00"
        for x in range(50):
            datas = basic_f1.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 4999)
            r3 = randint(0, 30)
            r4 = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4})
            data_f1.append(datas)

        cups = "ES0012345678923456780F"
        ts = "2022-01-01 00:00:00"
        for x in range(70):
            datas = basic_f1.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 10)
            r3 = randint(0, 30)
            r4 = randint(0, 10)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'cups': cups})
            data_f1.append(datas)

        return data_f1

    @staticmethod
    def get_sample_data_with_decimals():
        basic_f1 = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2022-01-01 01:00:00",
            "tipo_medida": "p",
            "season": "W",
            "ai": 10.1,
            "ae": 10.2,
            "r1": 10.3,
            "r2": 10.4,
            "r3": 10.5,
            "r4": 10.6,
            "quality_ai": 0,
            "quality_ae": 0,
            "quality_r1": 0,
            "quality_r2": 0,
            "quality_r3": 0,
            "quality_r4": 0,
            "quality_res": 0,
            "quality_res2": 0,
            "method": 1,
        }

        data_f1 = [basic_f1.copy()]

        return data_f1

    @staticmethod
    def get_sample_p2d_data():
        basic_p2d = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2022-01-01 01:00:00",
            "tipo_medida": "p4",
            "season": "W",
            "ae": 11.8,
            "ai": 1.2,
            "r1": 10,
            "r2": 10,
            "r3": 10,
            "r4": 10,
            "quality_ai": 0,
            "quality_ae": 0,
            "quality_r1": 0,
            "quality_r2": 0,
            "quality_r3": 0,
            "quality_r4": 0,
            "quality_res": 0,
            "quality_res2": 0,
            "method": 1,
        }

        data_p2d = [basic_p2d.copy()]

        ts = "2022-01-01 00:15:00"
        for x in range(360):
            datas = basic_p2d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 4999)
            r3 = randint(0, 30)
            r4 = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4})
            data_p2d.append(datas)

        cups = "ES0012345678923456780F"
        ts = "2022-01-01 00:15:00"
        for x in range(360):
            datas = basic_p2d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 10)
            r3 = randint(0, 30)
            r4 = randint(0, 10)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'cups': cups})
            data_p2d.append(datas)

        return data_p2d

    @staticmethod
    def get_sample_f1qh_data():
        basic_f1qh = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2022-01-01 00:15:00",
            "tipo_medida": "p",
            "season": "W",
            "ae": 10,
            "ai": 10,
            "r1": 10,
            "r2": 10,
            "r3": 10,
            "r4": 10,
            "quality_ai": 0,
            "quality_ae": 0,
            "quality_r1": 0,
            "quality_r2": 0,
            "quality_r3": 0,
            "quality_r4": 0,
            "quality_res": 0,
            "quality_res2": 0,
            "method": 1,
        }

        data_f1qh = [basic_f1qh.copy()]

        ts = "2022-01-01 00:15:00"
        for x in range(50):
            datas = basic_f1qh.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 4999)
            r3 = randint(0, 30)
            r4 = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4})
            data_f1qh.append(datas)

        cups = "ES0012345678923456780F"
        ts = "2022-01-01 00:00:00"
        for x in range(70):
            datas = basic_f1qh.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 10)
            r3 = randint(0, 30)
            r4 = randint(0, 10)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'cups': cups})
            data_f1qh.append(datas)

        return data_f1qh

    @staticmethod
    def get_sample_data_pmest():
        basic_pmest = {
            "pm": "DK029141",
            "tipo_medida": 11,
            "timestamp": "2024-11-01 01:00:00",
            "season": 0,
            "method": 4,
            "ai": 10,
            "ae": 11,
            "r1": 12,
            "r2": 13,
            "r3": 14,
            "r4": 15
        }

        data_pmest = [basic_pmest.copy()]

        ts = "2024-11-01 01:00:00"
        for x in range(50):
            datas = basic_pmest.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            r1 = randint(0, 30)
            r2 = randint(0, 4999)
            r3 = randint(0, 30)
            r4 = randint(0, 4999)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4})
            data_pmest.append(datas)

        return data_pmest

    @staticmethod
    def get_sample_p5d_data():
        basic_p5d = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2020-01-01 01:00:00",
            "season": "W",
            "ae": 0,
            "ai": 0
        }
        data_p5d = [basic_p5d.copy()]

        ts = "2020-01-01 01:00:00"
        for x in range(50):
            datas = basic_p5d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            datas.update({'timestamp': ts, 'ai': ai, 'ae': ae})
            data_p5d.append(datas)

        cups = "ES0012345678923456780F"
        ts = "2020-01-01 00:00:00"
        for x in range(70):
            datas = basic_p5d.copy()
            ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            ai = randint(0, 5000)
            ae = randint(0, 2)
            datas.update({'cups': cups, 'timestamp': ts, 'ai': ai, 'ae': ae})
            data_p5d.append(datas)

        return data_p5d

    @staticmethod
    def get_sample_f5d_data(file_format='REE'):
        basic_f5d = {
            "cups": "ES0012345678912345670F",
            "timestamp": "2020-01-01 01:00:00",
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
        if file_format == 'CNMC':
            basic_f5d.update({'ao_fix': 1000, 'ai_fix': 1000})
        data_f5d = [basic_f5d.copy()]
        ts = "2020-01-01 01:00:00"
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

        cups = "ES0012345678923456780F"
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
    def get_sample_mcil345qh_data():
        return [{
            'cil': 'ES0291000000004444QR1F001',
            'timestamp': '2022-09-01 00:15:00',
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
            'cil': 'ES0291000000004444QR1F001',
            'timestamp': '2022-09-01 00:30:00',
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
            'timestamp': '2022-09-01 00:15:00',
            'season': 1,
            'ae': 200,
            'ai': 20,
            'r1': 11,
            'r2': 22,
            'r3': 33,
            'r4': 44,
            'read_type': 'R'
        },
        {
            'cil': 'ES0291000000005555QR1F001',
            'timestamp': '2022-09-01 00:30:00',
            'season': 1,
            'ae': 200,
            'ai': 20,
            'r1': 11,
            'r2': 22,
            'r3': 33,
            'r4': 44,
            'read_type': 'R'
        }
        ]

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
            'read_type': 'E'
            },
        ]

    @staticmethod
    def get_sample_cildat_data():
        return [{
            'cil': 'ES0291000000004444QR1F001',
            'reg_minetad': 'NBT44444444',
            'reg_provisional': '',
            'reg_definitivo': 'RA22-0000004444-2022',
            'cp': '17005',
            'potencia': 49.75,
            'nombre': 'CIL DE PRUEBAS GISCE',
            'numero_pss': '',
            'subgrupo': 'b.1.1',
            'tipo_punto': '4',
            'fecha_alta': datetime(2022, 10, 6),
            'fecha_baja': '',
            'tension': '05',
            'fecha_acta_servicio': datetime(2022, 10, 1),
            'propiedad_equipo': 'S'
            }]

    @staticmethod
    def get_sample_cupsdat_data():
        return [{
            'cups': 'ES0291000000004444QR1F',
            'descripcion': 'CUPS de Demo 01',
            'cif': 'X0004444',
            'distribuidor': '4444',
            'comercializador': '5555',
            'agree_tipo': '2',
            'agree_tensio': 'E2',
            'agree_tarifa': '6A',
            'agree_dh': 'G0',
            'alta_baja_tension': 'A',
            'provincia': 'GI',
            'potencia_p1': 400,
            'potencia_p2': 400,
            'potencia_p3': 400,
            'potencia_p4': 400,
            'potencia_p5': 400,
            'potencia_p6': 500,
            'cnae': '1091',
            'fecha_hora_inicio_vigencia': '2022-10-01 01',
            'fecha_hora_final_vigencia': '2022-10-17 00',
            'cp': '17005',
            'propiedad_equipo': 'S',
            'tension': '27'
        },
            {
            'cups': 'ES0291000000005555QR1F',
            'descripcion': 'CUPS de Demo 02',
            'cif': 'X0005555',
            'distribuidor': '4444',
            'comercializador': '5555',
            'agree_tipo': '2',
            'agree_tensio': 'E2',
            'agree_tarifa': '6A',
            'agree_dh': 'G0',
            'alta_baja_tension': 'A',
            'provincia': 'GI',
            'potencia_p1': 400,
            'potencia_p2': 400,
            'potencia_p3': 400,
            'potencia_p4': 400,
            'potencia_p5': 400,
            'potencia_p6': 500,
            'cnae': '1091',
            'fecha_hora_inicio_vigencia': '2022-10-17 01',
            'fecha_hora_final_vigencia': '',
            'cp': '17005',
            'propiedad_equipo': 'S',
            'tension': '27'
        }]

    @staticmethod
    def get_sample_cupsdat_data_isp_2024():
        res = SampleData().get_sample_cupsdat_data()
        res[0].update({'indicador_envio_medida': 'Q'})
        res[1].update({'indicador_envio_medida': 'Q'})
        return res

    @staticmethod
    def get_sample_cups45_data():
        return [{
            'cups': 'ES0291000000004444QR1F',
            'distribuidor': '4444',
            'comercializador': '5555',
            'agree_tipo': '5',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'provincia': 'GI',
            'potencia_p1': 4,
            'potencia_p2': 4,
            'potencia_p3': 5,
            'potencia_p4': 0,
            'potencia_p5': 0,
            'potencia_p6': 0,
            'telegestion': 'S',
            'fecha_hora_inicio_vigencia': '2022-10-01 01',
            'fecha_hora_final_vigencia': '2022-10-17 00',
            'cnae': '0968',
            'cp': '17005',
        },
            {
            'cups': 'ES0291000000005555QR1F',
            'distribuidor': '4444',
            'comercializador': '5555',
            'agree_tipo': '5',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'provincia': 'GI',
            'potencia_p1': 4,
            'potencia_p2': 4,
            'potencia_p3': 4,
            'potencia_p4': 0,
            'potencia_p5': 0,
            'potencia_p6': 0,
            'telegestion': 'S',
            'fecha_hora_inicio_vigencia': '2022-10-17 01',
            'fecha_hora_final_vigencia': '',
            'cnae': '0968',
            'cp': '17005',
        }]

    @staticmethod
    def get_sample_reobjeagrecl_data():
        return [{
            'distribuidora': '4444',
            'comercialitzadora': '5555',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'agree_tipo': '05',
            'provincia': 'HU',
            'tipus_demanda': '41',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'magnitud': 'AE',
            'energia_publicada': '100',
            'energia_proposada': '110',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '2',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.'
        },
        {
            'distribuidora': '4444',
            'comercialitzadora': '6666',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'agree_tipo': '05',
            'provincia': 'HU',
            'tipus_demanda': '00',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'magnitud': 'AE',
            'energia_publicada': 40,
            'energia_proposada': 50,
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'S',
            'motiu_receptor': '1',
            'comentari_receptor': False
        }
        ]

    @staticmethod
    def get_sample_reobjeincl_data():
        return [{
            'cups': 'ES0291000000004444QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'energia_entrant_publicada': 100,
            'energia_entrant_proposada': 110,
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '2',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.'
        },
        {
            'cups': 'ES0291000000005555QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'energia_entrant_publicada': 100,
            'energia_entrant_proposada': 100,
            'energia_sortint_publicada': 10,
            'energia_sortint_proposada': 20,
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '2',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.'
        }]

    @staticmethod
    def get_sample_reobje2_data():
        return [{
            'cups': 'ES0291000000004444QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'energia_publicada': '100',
            'energia_proposada': '110',
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '2',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.',
            'magnitud': 'AE'
        },
        {
            'cups': 'ES0291000000004444QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'energia_publicada': '100',
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '2',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.',
            'magnitud': 'AE'
        }]

    @staticmethod
    def get_sample_reobjecil_data():
        return [{
            'cil': 'ES0291000000004444QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'as_publicada': '100',
            'as_proposada': '110',
            'r2_publicada': '100',
            'r2_proposada': '110',
            'r3_publicada': '100',
            'r3_proposada': '110',
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'acceptacio': 'N',
            'motiu_receptor': '99',
            'comentari_receptor': 'La energia está correcta. A llorar a la llorería.',
        },
        {
            'cil': 'ES0291000000004444QR1F',
            'data_inici': '2024/01/01 01',
            'data_fi': '2024/02/01 00',
            'motiu_emissor': '100',
            'auto_obj': 'N',
            'acceptacio': 'N',
        }]

    @staticmethod
    def get_sample_obagrecl_data():
        return [{
            'distribuidora': '4444',
            'comercialitzadora': '5555',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'agree_tipo': '05',
            'provincia': 'HU',
            'tipus_demanda': '41',
            'periode': '2024/10',
            'motiu_emissor': '100',
            'magnitud': 'AE',
            'energia_publicada': '100',
            'energia_proposada': '110',
            'auto_obj': 'N'
        },
        {
            'distribuidora': '4444',
            'comercialitzadora': '6666',
            'agree_tensio': 'E0',
            'agree_tarifa': '2T',
            'agree_dh': 'E3',
            'agree_tipo': '05',
            'provincia': 'HU',
            'tipus_demanda': '00',
            'periode': '2024/10',
            'motiu_emissor': '100',
            'magnitud': 'AE',
            'energia_publicada': 40,
            'energia_proposada': 50,
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N'
        }
        ]

    @staticmethod
    def get_sample_obcups_data():
        return [{
            'cups': 'ES0291000000004444QR1F',
            'periode': '2024/10',
            'motiu_emissor': '100',
            'energia_publicada': '100',
            'energia_proposada': '110',
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'magnitud': 'AE'
        },
        {
            'cups': 'ES0291000000004444QR1F',
            'periode': '2024/10',
            'motiu_emissor': '100',
            'energia_publicada': '100',
            'comentari_emissor': 'Paga la energia, primer aviso.',
            'auto_obj': 'N',
            'magnitud': 'AE'
        }
        ]


with description('A P5D'):
    with it('is instance of P5D Class'):
        data = SampleData().get_sample_p5d_data()
        f = P5D(data)
        assert isinstance(f, P5D)

    with it('has its class methods'):
        data = SampleData().get_sample_p5d_data()
        f = P5D(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))
        assert isinstance(f.ai, (int, np.int64))
        assert isinstance(f.ae, (int, np.int64))
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

    with it('gets expected content'):
        data = SampleData().get_sample_p5d_data()
        f = P5D(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;2020/01/01 01:00;0;0;0'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

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
        assert isinstance(f.ai, (int, np.int64))
        assert isinstance(f.ae, (int, np.int64))
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

    with it('gets expected content'):
        data = SampleData().get_sample_f5d_data()
        f = F5D(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;2020/01/01 01:00;0;0;0;0;0;0;0;1;0;FE20214444'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

    with it('gets expected content when uses ZIP compression'):
        data = SampleData().get_sample_f5d_data()
        f = F5D(data, compression='zip')
        res = f.writer()
        expected = 'ES0012345678912345670F;2020/01/01 01:00;0;0;0;0;0;0;0;1;0;FE20214444'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected
        assert '.zip' in res

    with it('with CNMC format has its class methods'):
        data = SampleData().get_sample_f5d_data(file_format='CNMC')
        f = F5D(data, file_format='CNMC')
        res = f.writer()
        assert isinstance(f.ai_fix, (int, np.int64))
        assert isinstance(f.ao_fix, (int, np.int64))

    with it('with CNMC format gets expected content'):
        data = SampleData().get_sample_f5d_data(file_format='CNMC')
        f = F5D(data, file_format='CNMC')
        res = f.writer()
        expected = 'ES0012345678912345670F;2020/01/01 01:00;0;0;0;0;0;0;0;1;0;FE20214444;1000;1000'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

with description('An F1'):
    with it('is instance of F1 Class'):
        data = SampleData().get_sample_data()
        f = F1(data)
        assert isinstance(f, F1)

    with it('is a zip of raw files'):
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

    with it('gets expected content'):
        data = SampleData().get_sample_data()
        f = F1(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;11;2022/01/01 01:00:00;0;10;10;10;10;10;10;0;0;1;1'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

    with it('allows decimals if specified'):
        data = SampleData().get_sample_data_with_decimals()
        f = F1(data, allow_decimals=True)
        res = f.writer()
        expected = 'ES0012345678912345670F;11;2022/01/01 01:00:00;0;10.1;10.2;10.3;10.4;10.5;10.6;0;0;1;1'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

    with it('truncates decimals if not allow_decimals parameter is specified'):
        data = SampleData().get_sample_data_with_decimals()
        f = F1(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;11;2022/01/01 01:00:00;0;10;10;10;10;10;10;0;0;1;1'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

with description('An F1QH'):
    with it('is instance of F1QH Class'):
        data = SampleData().get_sample_f1qh_data()
        f = F1QH(data)
        assert isinstance(f, F1QH)

    with it('is a zip of raw files'):
        data = SampleData().get_sample_f1qh_data()
        f = F1QH(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_f1qh_data()
        f = F1QH(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))
        assert f.ai == f.total
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

    with it('gets expected content'):
        data = SampleData().get_sample_f1qh_data()
        f = F1QH(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;11;2022/01/01 00:15;0;10;10;10;10;10;10;0;0;1;1'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected


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
             'potencia_nominal': '2', 'codi_postal': '17007', 'subgrup': 'b11', 'emmagatzematge': '1111',
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
    with it('is instance of P1 Class'):
        data = SampleData().get_sample_data()
        f = P1(data)
        assert isinstance(f, P1)

    with it('is a zip file'):
        data = SampleData().get_sample_data()
        f = P1(data, distributor='9999')
        filepath = f.writer()
        assert zipfile.is_zipfile(filepath)
        assert f.zip_filename.endswith('.zip')

    with it('gets expected content'):
        data = SampleData().get_sample_data()
        f = P1(data)
        res = f.writer()
        expected = 'ES0012345678912345670F;11;2022/01/01 01:00:00;0;10;0;10;0;10;0;10;0;10;0;10;0;0;0;0;0;1;1'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected

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
    with it('is instance of P1D Class'):
        data = SampleData().get_sample_data()
        f = P1D(data)
        assert isinstance(f, P1D)

    with it('should have bz2 as a default compression'):
        data = SampleData().get_sample_data()
        f = P1D(data)
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        f1 = f.writer()
        assert isinstance(f1, str)

with description('A P2D'):
    with it('is instance of P2D Class'):
        data = SampleData().get_sample_p2d_data()
        f = P2D(data)
        assert isinstance(f, P2D)

    with it('should have bz2 as a default compression'):
        data = SampleData().get_sample_p2d_data()
        f = P2D(data)
        res = f.writer()
        assert isinstance(f.filename, str)
        assert '.bz2' in f.filename
        assert f.filename.endswith('.bz2')
        f1 = f.writer()
        assert isinstance(f1, str)

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
        # Version control causes file to be version 1 instead of 0
        assert f1.endswith('.1')

with description('A B5D'):
    with it('bz2 as a default compression'):
        f = B5D([{'cups': 'XDS', 'timestamp': datetime.now(), 'season': 1, 'ai': 0, 'factura': 123}], compression='bz2')
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
        # Version control causes file to be version 1 instead of 0
        assert f1.endswith('.1')

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

    with it('is a BZ2 file'):
        data = SampleData().get_sample_cumpelectro_data()
        f = CUMPELECTRO(data)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' in filepath

    with it('is a raw file if no compression is used'):
        data = SampleData().get_sample_cumpelectro_data()
        f = CUMPELECTRO(data, compression=False)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' not in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' not in filepath

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

    with it('is a BZ2 file'):
        data = SampleData().get_sample_cupselectro_data()
        f = CUPSELECTRO(data)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' in filepath

    with it('is a raw file if no compression is used'):
        data = SampleData().get_sample_cupselectro_data()
        f = CUPSELECTRO(data, compression=False)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' not in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' not in filepath

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

    with it('is a BZ2 file'):
        data = SampleData().get_sample_potelectro_data()
        f = POTELECTRO(data)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' in filepath

    with it('is a raw file if no compression is used'):
        data = SampleData().get_sample_potelectro_data()
        f = POTELECTRO(data, compression=False)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' not in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' not in filepath

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

    with it('is a BZ2 file'):
        data = SampleData().get_sample_enelectroaut_data()
        f = ENELECTROAUT(data)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' in filepath

    with it('is a raw file if no compression is used'):
        data = SampleData().get_sample_enelectroaut_data()
        f = ENELECTROAUT(data, compression=False)
        filepath = f.writer()
        assert isinstance(filepath, str)
        assert '.bz2' not in f.filename
        assert isinstance(f.filename, str)
        assert '.bz2' not in filepath

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
        assert isinstance(f.hours_per_cil, list)
        assert isinstance(f.ae, int)
        assert isinstance(f.r2, int)
        assert isinstance(f.r3, int)

    with it('has its expected content'):
        data = SampleData().get_sample_medidas_data()
        f = MEDIDAS(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F001;2022/09/01 01:00:00;1;10;2;3;;;R\n' \
                   'ES0291000000005555QR1F001;2022/09/01 01:00:00;1;40;4;6;;;E\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A CUPSDAT'):
    with it('is instance of CUPSDAT Class'):
        data = SampleData().get_sample_cupsdat_data()
        f = CUPSDAT(data)
        assert isinstance(f, CUPSDAT)

    with it('has its class methods'):
        data = SampleData().get_sample_cupsdat_data()
        f = CUPSDAT(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)
        assert f.number_of_cups == 2

    with it('has its expected content'):
        data = SampleData().get_sample_cupsdat_data()
        f = CUPSDAT(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F;CUPS de Demo 01;X0004444;4444;5555;2;' \
                   'E2;6A;G0;A;GI;400;400;400;400;400;500;1091;2022/10/01 01;2022/10/17 00;17005;S;27\n' \
                   'ES0291000000005555QR1F;CUPS de Demo 02;X0005555;4444;5555;2;' \
                   'E2;6A;G0;A;GI;400;400;400;400;400;500;1091;2022/10/17 01;3000/01/01 00;17005;S;27\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

    with it('has new field indicador_envio_medida if it is specified in function call'):
        data = SampleData().get_sample_cupsdat_data_isp_2024()
        f = CUPSDAT(data, include_measure_type_indicator=True)
        assert 'indicador_envio_medida' in f.columns

    with it('has its expected content when indicador_envio_medida is included'):
        data = SampleData().get_sample_cupsdat_data_isp_2024()
        f = CUPSDAT(data, include_measure_type_indicator=True)
        res = f.writer()
        expected = 'ES0291000000004444QR1F;CUPS de Demo 01;X0004444;4444;5555;2;' \
                   'E2;6A;G0;A;GI;400;400;400;400;400;500;1091;2022/10/01 01;2022/10/17 00;17005;S;27;Q\n' \
                   'ES0291000000005555QR1F;CUPS de Demo 02;X0005555;4444;5555;2;' \
                   'E2;6A;G0;A;GI;400;400;400;400;400;500;1091;2022/10/17 01;3000/01/01 00;17005;S;27;Q\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A CUPS45'):
    with it('is instance of CUPS45 Class'):
        data = SampleData().get_sample_cups45_data()
        f = CUPS45(data)
        assert isinstance(f, CUPS45)

    with it('has its class methods'):
        data = SampleData().get_sample_cups45_data()
        f = CUPS45(data)
        res = f.writer()
        assert isinstance(f.cups, list)
        assert isinstance(f.number_of_cups, int)

    with it('has its expected content'):
        data = SampleData().get_sample_cups45_data()
        f = CUPS45(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F;4444;5555;5;E0;2T;E3;GI;4;4;5;0;0;0;S;2022/10/01 01;2022/10/17 00;0968;17005\n' \
                   'ES0291000000005555QR1F;4444;5555;5;E0;2T;E3;GI;4;4;4;0;0;0;S;2022/10/17 01;3000/01/01 00;0968;17005\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

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
        expected = 'ES0291000000004444QR1F001;2022/09/01 01;1;90;0;1;2;3;4;R\n' \
                   'ES0291000000005555QR1F001;2022/09/01 01;1;180;0;11;22;33;44;R\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A MCIL345QH'):
    with it('is instance of MCIL345QH Class'):
        data = SampleData().get_sample_mcil345qh_data()
        f = MCIL345QH(data)
        assert isinstance(f, MCIL345QH)

    with it('has its class methods'):
        data = SampleData().get_sample_mcil345qh_data()
        f = MCIL345QH(data)
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
        data = SampleData().get_sample_mcil345qh_data()
        f = MCIL345QH(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F001;2022/09/01 00:15;1;90;0;1;2;3;4;R\n'\
                   'ES0291000000004444QR1F001;2022/09/01 00:30;1;90;0;1;2;3;4;R\n'\
                   'ES0291000000005555QR1F001;2022/09/01 00:15;1;180;0;11;22;33;44;R\n'\
                   'ES0291000000005555QR1F001;2022/09/01 00:30;1;180;0;11;22;33;44;R\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A CILDAT'):
    with it('is instance of CILDAT Class'):
        data = SampleData().get_sample_cildat_data()
        f = CILDAT(data)
        assert isinstance(f, CILDAT)

    with it('has its class methods'):
        data = SampleData().get_sample_cildat_data()
        f = CILDAT(data)
        res = f.writer()
        assert isinstance(f.cils, list)
        assert isinstance(f.number_of_cils, int)

    with it('gets expected content'):
        data = SampleData().get_sample_cildat_data()
        f = CILDAT(data)
        res = f.writer()
        expected = 'ES0291000000004444QR1F001;NBT44444444;;RA22-0000004444-2022;17005;49.75;' \
                   'CIL DE PRUEBAS GISCE;;b.1.1;4;20221006;30000101;05;20221001;S\n'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A REOBJEAGRECL'):
    with it('is instance of REOBJEAGRECL Class'):
        data = SampleData().get_sample_reobjeagrecl_data()
        f = REOBJEAGRECL(data)
        assert isinstance(f, REOBJEAGRECL)

    with it('gets expected content'):
        data = SampleData().get_sample_reobjeagrecl_data()
        f = REOBJEAGRECL(data)
        res = f.writer()
        expected = "4444;5555;E0;2T;E3;05;HU;41;2024/01/01 01;2024/02/01 00;100;AE;100;110;;N;N;2;La energia está correcta. A llorar a la llorería.\n" \
                   "4444;6666;E0;2T;E3;05;HU;00;2024/01/01 01;2024/02/01 00;100;AE;40;50;Paga la energia, primer aviso.;N;S;1;\n"
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A REOBJEINCL'):
    with it('is instance of REOBJEINCL Class'):
        data = SampleData().get_sample_reobjeincl_data()
        f = REOBJEINCL(data)
        assert isinstance(f, REOBJEINCL)

    with it('gets expected content'):
        data = SampleData().get_sample_reobjeincl_data()
        f = REOBJEINCL(data)
        res = f.writer()
        expected = "ES0291000000004444QR1F;2024/01/01 01;2024/02/01 00;100;100;110;;;Paga la energia, primer aviso.;N;N;2;La energia está correcta. A llorar a la llorería.\n" \
                   "ES0291000000005555QR1F;2024/01/01 01;2024/02/01 00;100;100;100;10.0;20.0;Paga la energia, primer aviso.;N;N;2;La energia está correcta. A llorar a la llorería.\n"
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A REOBJE2'):
    with it('is instance of REOBJE2 Class'):
        data = SampleData().get_sample_reobje2_data()
        f = REOBJE2(data)
        assert isinstance(f, REOBJE2)

    with it('gets expected content'):
        data = SampleData().get_sample_reobje2_data()
        f = REOBJE2(data)
        res = f.writer()
        expected = ("ES0291000000004444QR1F;2024/01/01 01;2024/02/01 00;100;100;110;Paga la energia, "
                    "primer aviso.;N;N;2;La energia está correcta. A llorar a la llorería.;AE\n"
                    "ES0291000000004444QR1F;2024/01/01 01;2024/02/01 00;100;100;;Paga la energia, "
                    "primer aviso.;N;N;2;La energia está correcta. A llorar a la llorería.;AE\n"
                    )
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('A REOBJECIL'):
    with it('is instance of REOBJECIL Class'):
        data = SampleData().get_sample_reobjecil_data()
        f = REOBJECIL(data)
        assert isinstance(f, REOBJECIL)

    with it('gets expected content'):
        data = SampleData().get_sample_reobjecil_data()
        f = REOBJECIL(data)
        res = f.writer()
        expected = ("ES0291000000004444QR1F;2024/01/01 01;2024/02/01 00;100;100;110;100;110;100;110;"
                    "Paga la energia, primer aviso.;N;N;99;La energia está correcta. A llorar a la llorería.\n"
                    "ES0291000000004444QR1F;2024/01/01 01;2024/02/01 00;100;;;;;;;;N;N;;\n")
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('An OBAGRECL'):
    with it('is instance of OBAGRECL Class'):
        data = SampleData().get_sample_obagrecl_data()
        f = OBAGRECL(data)
        assert isinstance(f, OBAGRECL)

    with it('gets expected content'):
        data = SampleData().get_sample_obagrecl_data()
        f = OBAGRECL(data)
        res = f.writer()
        expected = "4444;5555;E0;2T;E3;05;HU;41;2024/10;100;AE;100;110;;N\n" \
                   "4444;6666;E0;2T;E3;05;HU;00;2024/10;100;AE;40;50;Paga la energia, primer aviso.;N\n"
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('An OBCUPS'):
    with it('is instance of OBCUPS Class'):
        data = SampleData().get_sample_obcups_data()
        f = OBCUPS(data)
        assert isinstance(f, OBCUPS)

    with it('gets expected content'):
        data = SampleData().get_sample_obcups_data()
        f = OBCUPS(data)
        res = f.writer()
        expected = ("ES0291000000004444QR1F;2024/10;100;100;110;Paga la energia, "
                    "primer aviso.;N;AE\n"
                    "ES0291000000004444QR1F;2024/10;100;100;;Paga la energia, "
                    "primer aviso.;N;AE\n"
                    )
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False) == expected

with description('An PMEST'):
    with it('is instance of PMEST Class'):
        data = SampleData().get_sample_data_pmest()
        f = PMEST(data)
        assert isinstance(f, PMEST)

    with it('is a zip of raw files'):
        data = SampleData().get_sample_data_pmest()
        f = PMEST(data)
        res = f.writer()
        assert zipfile.is_zipfile(res)

    with it('has its class methods'):
        data = SampleData().get_sample_data_pmest()
        f = PMEST(data)
        res = f.writer()
        assert isinstance(f.total, (int, np.int64))
        assert f.ai == f.total

    with it('gets expected content'):
        data = SampleData().get_sample_data_pmest()
        f = PMEST(data)
        res = f.writer()
        # WARNING: timestamp is expressed as "yyyy/mm/dd HH" in file, but in dataframe is still ISO formatted
        expected = 'DK029141;11;2024-11-01 01:00:00;0;4;10;11;12;13;14;15'
        assert f.file[f.columns].to_csv(sep=';', header=None, index=False).split('\n')[0] == expected