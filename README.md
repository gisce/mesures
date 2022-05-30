# Mesures

:octocat: :hammer:
![](https://github.com/gisce/mesures/actions/workflows/python2-app.yml/badge.svg)
![](https://github.com/gisce/mesures/actions/workflows/python2-app.yml)
![](https://github.com/gisce/mesures/actions/workflows/python3-app.yml/badge.svg)
![](https://github.com/gisce/mesures/actions/workflows/python3-app.yml)

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
- `CUPSELECTRO`
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
