# Mesures

:octocat: :hammer:
[![Mesures](https://img.shields.io/badge/version-1.3.0-green.svg)](https://github.com/gisce/mesures/edit/master/README.md)

- Eina pel tractament de fitxers d'intercanvi de mesures entre [REE](https://www.ree.es) y participants
- Aporta el coneixement i formats necessaris per crear fitxers amb el format unificat i establert per l'Operador del sistema
- Afegeix suport per llegir i tractar de forma més entenedora y esquematitzada fitxers críptics

## Exemple de fàcil utilització:

- Importa per nom:
```python
  from mesures.p2d import P2D
```

- Consulta les capçaleres del fitxer:
```python
  mesures.p2d.columns
```

- Writer/reader unificats
```python
  p2d = P2D()
  p2d.writer()
```
## Suporta
- `A5D`
- `AUTOCONSUMO`
- `ALMACENACAU`
- `B5D`
- `CILCAU`
- `CUPSCAU`
- `F1`
- `P1`
- `P1D`
- `P2`
- `P2D`
- `P5D`
