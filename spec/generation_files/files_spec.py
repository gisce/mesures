from mamba import description, context, it
from expects import expect, equal
from mesures.f1 import F1
from sample_data_spec import get_sample_data


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

