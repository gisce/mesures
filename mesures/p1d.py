import os
from mesures.p1 import P1
from mesures.headers import P1_HEADER as columns

class P1D(P1):
    def __init__(self, data, distributor=None, comer=None):
        super(P1D, self).__init__(data, distributor)
        self.prefix = 'P1D'
        self.default_compression = 'bz2'
        self.comer = comer

    @property
    def filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    def writer(self):
        """
        P1D contains all curve measure in one file
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file['timestamp'] = self.file['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M:%S'))
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
