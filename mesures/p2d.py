from mesures.p2 import P2
from mesures.headers import P1_HEADER as columns

class P2D(P2):
    def __init__(self, data, distributor=None):
        super(P2D, self).__init__(data, distributor)
        self.prefix = 'P2D'
        self.default_compression = 'bz2'

    @property
    def filename(self):
        return "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    def writer(self):
        """
        P2D contains all curve measure in one file
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
