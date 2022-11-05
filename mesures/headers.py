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

CUPSELECTRO_HEADER = [
    'cups',                     # str(22)
    'cif_empresa',              # str(9)
    'codigo_solicitud',         # str(25)
    'version_solicitud',        # str(6)
    'fecha',                    # str(10)
    'requiere_f3',              # char(1)
    'nuevo_suministro'          # char(1)
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

MEDIDAS_HEADER = [
    'cil',                  # str(25)
    'timestamp',            # str(aaaa/mm/dd hh:mm:ss)
    'season',               # str(1) in ('0' for winter, '1' for summer)
    'ae',                   # int(10)
    'r2',                   # int(10)
    'r3',                   # int(10)
    'power_factor',         # float(1*n.3*n)
    'power_factor_type',    # str(1) in ('0' for capacitive, '1' for inductive)
    'read_type'             # str(1) in ('E' for estimated, 'R' for real)
]

CUPSDAT_HEADER = [
    'cups',                         # str(22)
    'descripcion',                  # str(60)
    'cif',                          # str(9)
    'distribuidor',                 # str(4)
    'comercializador',              # str(4)
    'tipo',                         # str(1) in ('1', '2', '3')
    'tensio',                       # str(2)
    'tarifa',                       # str(2)
    'dh',                           # str(2)
    'alta_baja_tension',            # str(1) in ('A', 'B')
    'provincia',                    # str(2)
    'potencia_p1',                  # int(6) kW
    'potencia_p2',                  # int(6) kW
    'potencia_p3',                  # int(6) kW
    'potencia_p4',                  # int(6) kW
    'potencia_p5',                  # int(6) kW
    'potencia_p6',                  # int(6) kW
    'cnae',                         # str(5)
    'fecha_hora_inicio_vigencia',   # str(aaaa/mm/dd hh)
    'fecha_hora_final_vigencia',    # str(aaaa/mm/dd hh)
    'cp',                           # str(5)
    'propiedad_equipo',             # str(1) in ('S', 'N')
    'tension'                       # str(2)
]

CUPS45_HEADER = [
    'cups',                         # str(22)
    'distribuidor',                 # str(4)
    'comercializador',              # str(4)
    'tipo',                         # str(1) in ('4', '5')
    'tensio',                       # str(2)
    'tarifa',                       # str(2)
    'dh',                           # str(2)
    'provincia',                    # str(2)
    'potencia_p1',                  # int(6) kW
    'potencia_p2',                  # int(6) kW
    'potencia_p3',                  # int(6) kW
    'potencia_p4',                  # int(6) kW
    'potencia_p5',                  # int(6) kW
    'potencia_p6',                  # int(6) kW
    'telegestion',                  # str(1) in ('S', 'N')
    'fecha_hora_inicio_vigencia',   # str(aaaa/mm/dd hh)
    'fecha_hora_final_vigencia',    # str(aaaa/mm/dd hh)
    'cnae',                         # str(5)
    'cp',                           # str(5)
]

MCIL345_HEADER = [
    'cil',                  # str(25) CUPS + 3 digits ('001' style)
    'timestamp',            # str(aaaa/mm/dd hh)
    'season',               # str(1) in ('0' for winter, '1' for summer)
    'ae',                   # int(10)
    'ai',                   # int(10)
    'r1',                   # int(10)
    'r2',                   # int(10)
    'r3',                   # int(10)
    'r4',                   # int(10)
    'read_type'             # str(1) in ('E' for estimated, 'R' for real)
]

CILDAT_HEADER = [
    'cil',                  # str(25)
    'reg_minetad',          # str(25)
    'reg_provisional',      # str(25)
    'reg_definitivo',       # str(25)
    'cp',                   # str(5)
    'potencia',             # float(7*n.3*n) (kW)
    'nombre',               # str(100)
    'numero_pss',           # str(5)
    'subgrupo',             # str(5)
    'tipo_punto',           # str(1) ('3' / '4' / '5')
    'fecha_alta',           # str(aaammdd)
    'fecha_baja',           # str(aaammdd)
    'tension',              # str(2)
    'fecha_acta_servicio',  # str(aaammdd)
    'propiedad_equipo',     # str(1) ('S' / 'N')
]
