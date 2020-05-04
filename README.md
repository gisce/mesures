# Mesures

### En fase de desenvolupament :octocat: :hammer:
[![Mesures](https://img.shields.io/badge/version-0.0.1-orange.svg)](https://github.com/gisce/mesures/edit/master/README.md)

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
