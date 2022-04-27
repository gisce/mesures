# Mesures

:octocat: :hammer:
[![Mesures](https://img.shields.io/badge/version-1.8.1-green.svg?style=flat&logo=python)](https://pypi.org/project/mesures/)

- Eina pel tractament de fitxers d'intercanvi de mesures entre [REE](https://www.ree.es) y participants del sector elèctric.
- Aporta el coneixement i els formats necessaris per a crear fitxers amb el format unificat i establert per l'Operador del Sistema.
- Afegeix suport per a llegir i tractar de forma més entenedora y esquematitzada fitxers críptics.

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
- `AGRECL`
- `ALMACENACAU`
- `AUTOCONSUMO`
- `B5D`
- `CILCAU`
- `CUMPELECTRO`
- `CUPSCAU`
- `ENELECTROAUT`
- `F1`
- `F3`
- `F5`
- `F5D`
- `P1`
- `P1D`
- `P2`
- `P2D`
- `P5D`
- `PMEST`
- `POTELECTRO`

## Publicar versió a Pipy

`python setup.py sdist`
`twine upload -r pypi dist/*`
