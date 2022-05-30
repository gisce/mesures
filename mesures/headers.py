# -*- coding: utf-8 -*-
P5D_HEADER = [
    'cups',
    'timestamp',
    'season',
    'ai',
    'ae'
]

F5D_HEADER = [
    'cups',
    'timestamp',
    'season',
    'ai',
    'ae',
    'r1',
    'r2',
    'r3',
    'r4',
    'method',
    'firmeza',
    'factura'
]

P1_HEADER = [
    'cups',
    'tipo_medida',
    'timestamp',
    'season',
    'ai',
    'quality_ai',
    'ae',
    'quality_ae',
    'r1',
    'quality_r1',
    'r2',
    'quality_r2',
    'r3',
    'quality_r3',
    'r4',
    'quality_r4',
    'res',
    'quality_res',
    'res2',
    'quality_res2',
    'method',
    'firmeza'
]

P2_HEADER = [
    'cups',
    'tipo_medida',
    'timestamp',
    'season',
    'ai',
    'quality_ai',
    'ae',
    'quality_ae',
    'r1',
    'quality_r1',
    'r2',
    'quality_r2',
    'r3',
    'quality_r3',
    'r4',
    'quality_r4',
    'res',
    'quality_res',
    'res2',
    'quality_res2',
    'method'
]

F1_HEADER = [
    'cups',
    'tipo_medida',
    'timestamp',
    'season',
    'ai',
    'ae',
    'r1',
    'r2',
    'r3',
    'r4',
    'res',
    'res2',
    'method',
    'firmeza'
]

AUTOCONSUMO_HEADER = [
    'cau',
    'miteco',
    'reg_auto_prov',
    'reg_auto_def',
    'tipus_autoconsum',
    'tipus_antiabocament',
    'nom',
    'configuracio_mesura',
    'potencia_nominal',
    'codi_postal',
    'subgrup',
    'emmagatzematge',
    'data_alta',
    'data_baixa'
]

CUPSCAU_HEADER = [
    'cau',
    'cups',
    'tipus_consum',
    'data_alta',
    'data_baixa',
    'comentari'
]

CILCAU_HEADER = [
    'cau',
    'cil',
    'data_alta',
    'data_baixa',
    'comentari'
]

ALMACENACAU_HEADER = [
    'cau',
    'potencia_nominal',
    'energia_emmagatzemable',
    'tecnologia_emmagatzematge',
    'data_alta',
    'data_baixa',
    'comentari'
]

AGRECL_HEADER = [
    'origen',
    'tipus_operacio',
    'distribuidora',
    'comercialitzadora',
    'tensio',
    'tarifa',
    'dh',
    'tipo',
    'provincia',
    'tipus_demanda',
    'data_alta',
    'data_baixa'
]

A5D_HEADER = [
    'cups',
    'timestamp',
    'season',
    'ai',
    'ae',
    'r1',
    'r2',
    'r3',
    'r4',
    'method',
    'firmeza',
    'factura'
]

B5D_HEADER = [
    'cups',
    'timestamp',
    'season',
    'ai',
    'ae',
    'r1',
    'r2',
    'r3',
    'r4',
    'method',
    'firmeza',
    'factura'
]

PMEST_HEADER = [
    'pm',
    'tipo_medida',
    'timestamp',
    'season',
    'method',
    'ai',
    'ae',
    'r1',
    'r2',
    'r3',
    'r4'
]

CUMPELECTRO_HEADER = [
    'cups',                     # str(22)
    'cif_empresa',              # str(9)
    'codigo_solicitud',         # str(25)
    'version_solicitud',        # str(6)
    'electrointensivo_n1',      # str(1)
    'electrointensivo_n2',      # str(1)
    'electrointensivo_n3',      # str(1)
    'contrato_vigente_n1',      # str(1)
    'contrato_vigente_n2',      # str(1)
    'contrato_vigente_n3',      # str(1)
    'corriente_pagos_n1',       # str(1)
    'corriente_pagos_n2',       # str(1)
    'corriente_pagos_n3',       # str(1)
    'cargos_facturados_n1_p1',  # float(10.2)
    'cargos_facturados_n1_p2',  # float(10.2)
    'cargos_facturados_n1_p3',  # float(10.2)
    'cargos_facturados_n1_p4',  # float(10.2)
    'cargos_facturados_n1_p5',  # float(10.2)
    'cargos_facturados_n1_p6',  # float(10.2)
    'cargos_facturados_n2_p1',  # float(10.2)
    'cargos_facturados_n2_p2',  # float(10.2)
    'cargos_facturados_n2_p3',  # float(10.2)
    'cargos_facturados_n2_p4',  # float(10.2)
    'cargos_facturados_n2_p5',  # float(10.2)
    'cargos_facturados_n2_p6',  # float(10.2)
    'cargos_facturados_n3_p1',  # float(10.2)
    'cargos_facturados_n3_p2',  # float(10.2)
    'cargos_facturados_n3_p3',  # float(10.2)
    'cargos_facturados_n3_p4',  # float(10.2)
    'cargos_facturados_n3_p5',  # float(10.2)
    'cargos_facturados_n3_p6',  # float(10.2)
    'peajes_facturados_n1_p1',  # float(10.2)
    'peajes_facturados_n1_p2',  # float(10.2)
    'peajes_facturados_n1_p3',  # float(10.2)
    'peajes_facturados_n1_p4',  # float(10.2)
    'peajes_facturados_n1_p5',  # float(10.2)
    'peajes_facturados_n1_p6',  # float(10.2)
    'peajes_facturados_n2_p1',  # float(10.2)
    'peajes_facturados_n2_p2',  # float(10.2)
    'peajes_facturados_n2_p3',  # float(10.2)
    'peajes_facturados_n2_p4',  # float(10.2)
    'peajes_facturados_n2_p5',  # float(10.2)
    'peajes_facturados_n2_p6',  # float(10.2)
    'peajes_facturados_n3_p1',  # float(10.2)
    'peajes_facturados_n3_p2',  # float(10.2)
    'peajes_facturados_n3_p3',  # float(10.2)
    'peajes_facturados_n3_p4',  # float(10.2)
    'peajes_facturados_n3_p5',  # float(10.2)
    'peajes_facturados_n3_p6'   # float(10.2)
]

POTELECTRO_HEADER = [
    'cups',                     # str(22)
    'cif_empresa',              # str(9)
    'codigo_solicitud',         # str(25)
    'version_solicitud',        # str(6)
    'potencia_n-1_p1',          # float(6.1)
    'potencia_n-1_p2',          # float(6.1)
    'potencia_n-1_p3',          # float(6.1)
    'potencia_n-1_p4',          # float(6.1)
    'potencia_n-1_p5',          # float(6.1)
    'potencia_n-1_p6',          # float(6.1)
    'potencia_n-2_p1',          # float(6.1)
    'potencia_n-2_p2',          # float(6.1)
    'potencia_n-2_p3',          # float(6.1)
    'potencia_n-2_p4',          # float(6.1)
    'potencia_n-2_p5',          # float(6.1)
    'potencia_n-2_p6',          # float(6.1)
    'potencia_n-3_p1',          # float(6.1)
    'potencia_n-3_p2',          # float(6.1)
    'potencia_n-3_p3',          # float(6.1)
    'potencia_n-3_p4',          # float(6.1)
    'potencia_n-3_p5',          # float(6.1)
    'potencia_n-3_p6',          # float(6.1)
    'potencia_proyectada_p1',   # float(6.1)
    'potencia_proyectada_p2',   # float(6.1)
    'potencia_proyectada_p3',   # float(6.1)
    'potencia_proyectada_p4',   # float(6.1)
    'potencia_proyectada_p5',   # float(6.1)
    'potencia_proyectada_p6',   # float(6.1)
    'energia_proyectada_p1',    # int(10)
    'energia_proyectada_p2',    # int(10)
    'energia_proyectada_p3',    # int(10)
    'energia_proyectada_p4',    # int(10)
    'energia_proyectada_p5',    # int(10)
    'energia_proyectada_p6'     # int(10)
]

ENELECTROAUT_HEADER = [
    'cups',                         # str(22)
    'cif_empresa',                  # str(9)
    'codigo_solicitud',             # str(25)
    'version_solicitud',            # str(6)
    'energia_n-1_p1',               # int(10)
    'energia_n-1_p2',               # int(10)
    'energia_n-1_p3',               # int(10)
    'energia_n-1_p4',               # int(10)
    'energia_n-1_p5',               # int(10)
    'energia_n-1_p6',               # int(10)
    'energia_n-2_p1',               # int(10)
    'energia_n-2_p2',               # int(10)
    'energia_n-2_p3',               # int(10)
    'energia_n-2_p4',               # int(10)
    'energia_n-2_p5',               # int(10)
    'energia_n-2_p6',               # int(10)
    'energia_n-3_p1',               # int(10)
    'energia_n-3_p2',               # int(10)
    'energia_n-3_p3',               # int(10)
    'energia_n-3_p4',               # int(10)
    'energia_n-3_p5',               # int(10)
    'energia_n-3_p6',               # int(10)
    'autoconsumida_proyectada_p1',  # int(10)
    'autoconsumida_proyectada_p2',  # int(10)
    'autoconsumida_proyectada_p3',  # int(10)
    'autoconsumida_proyectada_p4',  # int(10)
    'autoconsumida_proyectada_p5',  # int(10)
    'autoconsumida_proyectada_p6'   # int(10)
]

F3_HEADER = [
    'cups',         # str(22)
    'timestamp',    # str(aaaa/mm/dd hh:mm)
    'season',       # str(1)
    'ai',           # int(10)
    'ae',           # int(10)
    'method',       # int(2)
    'firmeza'       # int(1)
]
