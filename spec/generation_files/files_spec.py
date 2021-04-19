from mamba import description, context, it
from expects import expect, equal
from mesures.f1 import F1
from mesures.p1 import P1
from mesures.p1d import P1D
from spec.sample_data import get_sample_data


with description('An F1') as self:
    with it('instance of F1 Class'):
        data = get_sample_data()
        f = F1(data)
        assert isinstance(f, F1)

    with it('a zip of raw Files'):
        data = get_sample_data()
        f = F1(data)
        res = f.writer()
        import zipfile
        assert zipfile.is_zipfile(res)


with description('An P1') as self:
    with it('instance of P1 Class'):
        data = get_sample_data()
        f = P1(data)
        assert isinstance(f, P1)

    with it('instance of P1D Class'):
        data = get_sample_data()
        f = P1D(data)
        assert isinstance(f, P1D)
