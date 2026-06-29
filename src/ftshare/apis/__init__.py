"""ftshare-doc topic API mixins used by ``FtshareClient``."""

from .stock import StockApiMixin
from .hk import HkApiMixin
from .us import UsApiMixin
from .index import IndexApiMixin
from .etf import EtfApiMixin
from .fund import FundApiMixin
from .futures import FuturesApiMixin
from .bond import BondApiMixin
from .economic import EconomicApiMixin
from .llm_corpus import LlmCorpusApiMixin
from .spot import SpotApiMixin
from .forex import ForexApiMixin
from .unpublished import UnpublishedApiMixin

__all__ = [
    'StockApiMixin',
    'HkApiMixin',
    'UsApiMixin',
    'IndexApiMixin',
    'EtfApiMixin',
    'FundApiMixin',
    'FuturesApiMixin',
    'BondApiMixin',
    'EconomicApiMixin',
    'LlmCorpusApiMixin',
    'SpotApiMixin',
    'ForexApiMixin',
    'UnpublishedApiMixin',
]
