from __future__ import unicode_literals
import pandas as pd
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class BaseStream(object):
    """Memory-efficient batch aggregator.
    Parameters
    ----------
    aggregation_columns : list[str]
        Columns used as *group by* keys when accumulating.
    selection_columns : list[str]
        Full set of columns allowed in the final :class:`pandas.DataFrame`.
    sort_columns : list[str]
        Columns applied to :py:meth:`pandas.DataFrame.sort_values` before
        serialisation.
    dtype_map : dict, optional
        Column-to-dtype mapping applied to the final frame.
    """

    def __init__(self, selection_columns, aggregation_columns, aggregation_map, sort_columns, dtype_map=None):
        # ['cups', 'timestamp', 'season', 'firmeza', 'method']
        self.aggregation_columns = aggregation_columns
        # ex. {'ai': 'sum', 'ae': 'sum', 'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        self.aggregation_map = aggregation_map
        # Initial columns
        self.selection_columns = selection_columns
        # ['timestamp', 'cups']
        self.sort_columns = sort_columns
        self.dtype_map = dtype_map or {}

        self.numeric_cols = [
            c for c in self.selection_columns
            if c not in self.aggregation_columns
        ]

        # Lazily materialised DataFrame placeholder
        # setattr(self, self.frame_attr, pd.DataFrame(columns=self.selection_columns))
        self._frame_cache = pd.DataFrame(columns=self.selection_columns)
        # self.data_frame = pd.DataFrame(columns=self.selection_columns)

        # Incremental aggregation bucket
        # key_tuple  ->  list[aggregated numeric values]
        numeric_len = len(self.selection_columns) - len(self.aggregation_columns)
        self._agg = defaultdict(lambda: [0] * numeric_len)
        self._min_ts = None
        self._max_ts = None

    def add_chunk(self, chunk):
        """Add a batch of records.
        Each *chunk* is a ``list`` of ``dict`` where keys are columns.
        Missing numeric columns are filled with ``0`` to keep the schema
        consistent.
        """
        if not chunk:
            return True

        df = pd.DataFrame(chunk)
        if df.empty:
            return True

        # Track min/max timestamp if present (used for filenames)
        if "timestamp" in df.columns:
            t_min, t_max = df["timestamp"].min(), df["timestamp"].max()
            if self._min_ts is None or t_min < self._min_ts:
                self._min_ts = t_min
            if self._max_ts is None or t_max > self._max_ts:
                self._max_ts = t_max

        grouped = (df.groupby(self.aggregation_columns, sort=False,
                              observed=True)
                   .agg(self.aggregation_map)
                   .reset_index())

        for _, row in grouped.iterrows():
            key = tuple(row[c] for c in self.aggregation_columns)
            bucket = self._agg[key]
            for idx, col in enumerate(self.numeric_cols):
                bucket[idx] += int(row[col])

        return True

    def _materialise(self):
        if not self._agg:
            return self._frame_cache

        rows = []
        from six import iteritems
        for key, vals in iteritems(self._agg):
            row = dict(zip(self.aggregation_columns, key))
            row.update(dict(zip(self.numeric_cols, vals)))
            rows.append(row)

        df = pd.DataFrame.from_records(rows, columns=self.selection_columns)

        for col, typ in self.dtype_map.items():
            if col in df.columns:
                df[col] = df[col].astype(typ)

        df.sort_values(self.sort_columns, inplace=True)
        self._frame_cache = df
        # setattr(self, self.frame_attr, df)
        return df

    @property
    def data_frame(self):  # noqa: D401
        """Aggregated :class:`pandas.DataFrame` (materialised on first use)."""
        return self._materialise()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
