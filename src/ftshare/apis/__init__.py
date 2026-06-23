"""Business-domain API mixins used by ``FtshareClient``."""

from .corporate import CorporateApiMixin
from .economic import EconomicApiMixin
from .etf import EtfApiMixin
from .finance import FinanceApiMixin
from .fund import FundApiMixin
from .futures import FuturesApiMixin
from .global_index import GlobalIndexApiMixin
from .goodwill import GoodwillApiMixin
from .hk import HkApiMixin
from .holder import HolderApiMixin
from .index import IndexApiMixin
from .market import MarketApiMixin
from .pledge import PledgeApiMixin
from .stock import StockApiMixin

__all__ = [
    'CorporateApiMixin',
    'EconomicApiMixin',
    'EtfApiMixin',
    'FinanceApiMixin',
    'FundApiMixin',
    'FuturesApiMixin',
    'GlobalIndexApiMixin',
    'GoodwillApiMixin',
    'HkApiMixin',
    'HolderApiMixin',
    'IndexApiMixin',
    'MarketApiMixin',
    'PledgeApiMixin',
    'StockApiMixin',
]
