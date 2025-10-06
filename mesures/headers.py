# -*- coding: utf-8 -*-
# Valid for A5D and B5D
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

ALMACENACAU_HEADER = [
    'cau',
    'potencia_nominal',
    'energia_emmagatzemable',
    'tecnologia_emmagatzematge',
    'data_alta',
    'data_baixa',
    'comentari'
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
    'data_baixa',
    'estat'
]

CILCAU_HEADER = [
    'cau',
    'cil',
    'data_alta',
    'data_baixa',
    'comentari'
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

CUPSCAU_HEADER = [
    'cau',
    'cups',
    'tipus_consum',
    'data_alta',
    'data_baixa',
    'comentari'
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

CUPSDAT_HEADER_2024 = CUPSDAT_HEADER + [
    'indicador_envio_medida'        # str(1) in ('Q', 'H')
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

F1_HEADER = [
    'cups',         # str(22)
    'tipo_medida',  # str(2) (always '11')
    'timestamp',    # str(aaaa/mm/dd hh:mm:ss)
    'season',       # str(1) in ('0' for winter, '1' for summer)
    'ai',           # int (kWh)
    'ae',           # int (kWh)
    'r1',           # int (kWh)
    'r2',           # int (kWh)
    'r3',           # int (kWh)
    'r4',           # int (kWh)
    'res',          # int
    'res2',         # int
    'method',       # str(1) in ('1' for 'Medidas firmes en configuración principal',
                    #            '2' for 'Medidas firmes en configuración redundante'),
                    #            '3' for 'Medidas firmes de equipos de medida en configuración comprobante'),
                    #            '4' for 'Medidas provisionales en configuración principal'),
                    #            '5' for 'Medidas provisionales en configuración redundante'),
                    #            '6' for 'Medidas provisionales en configuración comprobante'),
                    # De 1 a 6 de acuerdo al cálculo de mejor de energía en punto frontera.
                    #            '7' for 'Estimación de energía horaria basada en el histórico del punto de medida
                    #                     principal modulado con su saldo'),
                    #            '8' for 'Estimación de energía con perfil plano a partir de cierres de ATR'),
                    #            '9' for 'Estimación basada en histórico del punto de medida principal (sin datos de
                    #                     saldo o de cierre de ATR)'),
                    #            '10' for 'Estimación técnicamente justificada tras incidencia en el equipo de medida'),
                    #            '11' for 'Estimación de energía horaria realizada basada en un factor de utilización
                    #                      del 33%'),
                    #            '22' for 'Estimación que penaliza para clientes tipo 1 y 2'))
                    # De 7 a 11 para estimaciones de puntos frontera de clientes tipo 1 y 2.
    'firmeza'       # str(1) in ('0' for 'No firme', '1' for 'Firme')
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

F5_HEADER = [
    'cups',         # str(22)
    'timestamp',    # str(aaaa/mm/dd hh:mm)
    'season',       # str(1) in ('0' for winter, '1' for summer)
    'ai',           # int (Wh)
    'ae',           # int (Wh)
    'r1',           # int (Wh)
    'r2',           # int (Wh)
    'r3',           # int (Wh)
    'r4',           # int (Wh)
    'method',       # str(1) in ('1' for 'Medida real válida',
                    #            '2' for 'Medida perfilada correspondiente a un cierre real'),
                    #            '3' for 'Medida real ajustada a un cierre real'),
                    #            '4' for 'Medida perfilada correspondiente a auto-lectura de cliente'),
                    #            '5' for 'Estimación por consumo histórico del año anterior perfilado'),
                    #            '6' for 'Estimación por factor de utilización perfilado'))
    'firmeza',      # str(1) in ('0' for 'No firme', '1' for 'Firme')
]

F5D_HEADER = F5_HEADER + [
    'factura'       # str
]

MAGCL_HEADER = [
    'distribuidora',        # str(4)
    'comercialitzadora',    # str(4)
    'agree_tensio',         # str(2)
    'agree_tarifa',         # str(2)
    'agree_dh',             # str(2)
    'agree_tipo',           # str(2)
    'provincia',            # str(2)
    'tipus_demanda',        # str(2)
    'timestamp',            # str(aaaa/mm/dd hh:mm)
    'estacio',              # str(1) in ('0' for winter, '1' for summer)
    'magnitud',             # str(2)
    'consum',               # int(10)
    'n_punts',              # int(7)
    'm_iec_real',           # int(10)
    'n_iec_real',           # int(7)
    'm_iec_estimada',       # int(10)
    'n_iec_estimada',       # int(7)
    'm_integrats_real',     # int(10)
    'n_integrats_real',     # int(7)
    'm_integrats_estimada', # int(10)
    'n_integrats_estimada'  # int(7)
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

OBAGRECL_HEADER = [
    'distribuidora',        # str(4)
    'comercialitzadora',    # str(4)
    'agree_tensio',         # str(2)
    'agree_tarifa',         # str(2)
    'agree_dh',             # str(2)
    'agree_tipo',           # str(2)
    'provincia',            # str(2)
    'tipus_demanda',        # str(3)
    'periode',              # str aaaa/mm
    'motiu_emissor',        # str(3)
    'magnitud',             # str(2) AE/AS
    'energia_publicada',    # str(10) kWh
    'energia_proposada',    # str(10) kWh
    'comentari_emissor',    # str(255)
    'auto_obj'              # str(1) S/N
]

OBCIL_HEADER = [
    'cil',                  # str(25)
    'periode',              # str aaaa/mm
    'motiu_emissor',        # str(3)
    'ae_publicada',         # str(10) kWh
    'ae_proposada',         # str(10) kWh
    'r2_publicada',         # str(10) kVArh
    'r2_proposada',         # str(10) kVArh
    'r3_publicada',         # str(10) kVArh
    'r3_proposada',         # str(10) kVArh
    'comentari_emissor',    # str(255)
    'auto_obj'              # str(1) S/N
]

OBCUPS_HEADER = [
    'cups',                 # str(22)
    'periode',              # str aaaa/mm
    'motiu_emissor',        # str(3)
    'energia_publicada',    # str(10) kWh
    'energia_proposada',    # str(10) kWh
    'comentari_emissor',    # str(255)
    'auto_obj',             # str(1) S/N
    'magnitud'              # str(2) AS/AE
]

P1_HEADER = [
    'cups',          # str(22)
    'tipo_medida',   # str(2) (always '11')
    'timestamp',     # str(aaaa/mm/dd hh:mm:ss)
    'season',        # str(1) in ('0' for winter, '1' for summer)
    'ai',            # float(10*n.3*n) (kWh)
    'quality_ai',    # str(3)
    'ae',            # float(10*n.3*n) (kWh)
    'quality_ae',    # str(3)
    'r1',            # float(10*n.3*n) (kWh)
    'quality_r1',    # str(3)
    'r2',            # float(10*n.3*n) (kWh)
    'quality_r2',    # str(3)
    'r3',            # float(10*n.3*n) (kWh)
    'quality_r3',    # str(3)
    'r4',            # float(10*n.3*n) (kWh)
    'quality_r4',    # str(3)
    'res',           # float(10*n.3*n)
    'quality_res',   # str(3)
    'res2',          # float(10*n.3*n)
    'quality_res2',  # str(3)
    'method',        # str(1) in ('1' for 'Medidas firmes en configuración principal',
                     #            '2' for 'Medidas firmes en configuración redundante'),
                     #            '3' for 'Medidas firmes de equipos de medida en configuración comprobante'),
                     #            '4' for 'Medidas provisionales en configuración principal'),
                     #            '5' for 'Medidas provisionales en configuración redundante'),
                     #            '6' for 'Medidas provisionales en configuración comprobante'),
                     # De 1 a 6 de acuerdo al cálculo de mejor de energía en punto frontera.
                     #            '7' for 'Estimación de energía horaria basada en el histórico del punto de medida
                     #                     principal modulado con su saldo'),
                     #            '8' for 'Estimación de energía con perfil plano a partir de cierres de ATR'),
                     #            '9' for 'Estimación basada en histórico del punto de medida principal (sin datos de
                     #                     saldo o de cierre de ATR)'),
                     #            '10' for 'Estimación técnicamente justificada tras incidencia en el equipo de medida'),
                     #            '11' for 'Estimación de energía horaria realizada basada en un factor de utilización
                     #                      del 33%'),
                     #            '22' for 'Estimación que penaliza para clientes tipo 1 y 2'))
                     # De 7 a 11 para estimaciones de puntos frontera de clientes tipo 1 y 2.
    'firmeza'        # str(1) in ('0' for 'No firme', '1' for 'Firme')
]

P2_HEADER = [
    'cups',          # str(22)
    'tipo_medida',   # str(2) (always '11')
    'timestamp',     # str(aaaa/mm/dd hh:mm:ss)
    'season',        # str(1) in ('0' for winter, '1' for summer)
    'ai',            # int (kWh)
    'quality_ai',    # str(3)
    'ae',            # int (kWh)
    'quality_ae',    # str(3)
    'r1',            # int (kWh)
    'quality_r1',    # str(3)
    'r2',            # int (kWh)
    'quality_r2',    # str(3)
    'r3',            # int (kWh)
    'quality_r3',    # str(3)
    'r4',            # int (kWh)
    'quality_r4',    # str(3)
    'res',           # int
    'quality_res',   # str(3)
    'res2',          # int
    'quality_res2',  # str(3)
    'method',        # str(1) in ('1' for 'Medidas firmes en configuración principal',
                     #            '2' for 'Medidas firmes en configuración redundante'),
                     #            '3' for 'Medidas firmes de equipos de medida en configuración comprobante'),
                     #            '4' for 'Medidas provisionales en configuración principal'),
                     #            '5' for 'Medidas provisionales en configuración redundante'),
                     #            '6' for 'Medidas provisionales en configuración comprobante'),
                     # De 1 a 6 de acuerdo al cálculo de mejor de energía en punto frontera.
                     #            '7' for 'Estimación de energía horaria basada en el histórico del punto de medida
                     #                     principal modulado con su saldo'),
                     #            '8' for 'Estimación de energía con perfil plano a partir de cierres de ATR'),
                     #            '9' for 'Estimación basada en histórico del punto de medida principal (sin datos de
                     #                     saldo o de cierre de ATR)'),
                     #            '10' for 'Estimación técnicamente justificada tras incidencia en el equipo de medida'),
                     #            '11' for 'Estimación de energía horaria realizada basada en un factor de utilización
                     #                      del 33%'),
                     #            '22' for 'Estimación que penaliza para clientes tipo 1 y 2'))
                     # De 7 a 11 para estimaciones de puntos frontera de clientes tipo 1 y 2.
]

P5D_HEADER = [
    'cups',         # str(22)
    'timestamp',    # str(aaaa/mm/dd hh:mm)
    'season',       # str(1) in ('0' for winter, '1' for summer)
    'ai',           # int (Wh)
    'ae'            # int (Wh)
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

REOBJEAGRECL_HEADER = [
    'distribuidora',        # str(4)
    'comercialitzadora',    # str(4)
    'agree_tensio',         # str(2)
    'agree_tarifa',         # str(2)
    'agree_dh',             # str(2)
    'agree_tipo',           # str(2)
    'provincia',            # str(2)
    'tipus_demanda',        # str(2)
    'data_inici',           # str aaaa/mm/dd hh
    'data_fi',              # str aaaa/mm/dd hh
    'motiu_emissor',        # str(3)
    'magnitud',             # str(3)
    'energia_publicada',    # str(10) kWh
    'energia_proposada',    # str(10) kWh
    'comentari_emissor',    # str(255)
    'auto_obj',             # str(1) S/N
    'acceptacio',           # str(1) S/N
    'motiu_receptor',       # str(1)
    'comentari_receptor'    # str(255)
]

REOBJEINCL_HEADER = [
    'cups',                         # str(22)
    'data_inici',                   # str aaaammdd hh
    'data_fi',                      # str aaaammdd hh
    'motiu_emissor',                # str(3)
    'energia_entrant_publicada',    # str(10) kWh
    'energia_entrant_proposada',    # str(10) kWh
    'energia_sortint_publicada',    # str(10) kWh
    'energia_sortint_proposada',    # str(10) kWh
    'comentari_emissor',            # str(255)
    'auto_obj',                     # str(1) S/N
    'acceptacio',                   # str(1) S/N
    'motiu_receptor',               # str(2)
    'comentari_receptor'            # str(255)
]

REOBJE2_HEADER = [
    'cups',                         # str(22)
    'data_inici',                   # str aaaammdd hh
    'data_fi',                      # str aaaammdd hh
    'motiu_emissor',                # str(3)
    'energia_publicada',            # str(10) kWh
    'energia_proposada',            # str(10) kWh
    'comentari_emissor',            # str(255)
    'auto_obj',                     # str(1) S/N
    'acceptacio',                   # str(1) S/N
    'motiu_receptor',               # str(2)
    'comentari_receptor',           # str(255)
    'magnitud'                      # str(2) AS/AE
]

REOBJECIL_HEADER = [
    'cil',                          # str(22)
    'data_inici',                   # str aaaammdd hh
    'data_fi',                      # str aaaammdd hh
    'motiu_emissor',                # str(3)
    'as_publicada',                 # str(10) kWh
    'as_proposada',                 # str(10) kWh
    'r2_publicada',                 # str(10) kVArh
    'r2_proposada',                 # str(10) kVArh
    'r3_publicada',                 # str(10) kVArh
    'r3_proposada',                 # str(10) kVArh
    'comentari_emissor',            # str(255)
    'auto_obj',                     # str(1) S/N
    'acceptacio',                   # str(1) S/N
    'motiu_receptor',               # str(2)
    'comentari_receptor'            # str(255)
]