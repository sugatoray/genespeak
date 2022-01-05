from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseTextEncodingStrategy(object):
    name: str
    binary_string_length: int


class ASCIITextEncodingStrategy(BaseTextEncodingStrategy):
    name: str = "ascii"
    binary_string_length: int = 8

    def __init__(self):
        super().__init__(self.name, self.binary_string_length)


class UTF8TextEncodingStrategy(BaseTextEncodingStrategy):
    name: str = "utf-8"
    binary_string_length: int = 24

    def __init__(self):
        super().__init__(self.name, self.binary_string_length)


@dataclass
class TextEncodingStrategies:
    ascii = ASCIITextEncodingStrategy()
    utf8 = UTF8TextEncodingStrategy()


AVAILABLE_STRATEGY_NAMES = [s for s in dir(TextEncodingStrategies) if not s.startswith("_")]  # ["ascii", "utf8"]
DEFAULT_STRATEGY_NAME = "ascii"

def set_strategy(strategy_name: Optional[str]=None):
    """Returns a text-encoding strategy by name."""
    if strategy_name:
        strategy_name = strategy_name.replace("-", "")
    if (strategy_name is None) or (strategy_name not in AVAILABLE_STRATEGY_NAMES):
        strategy_name = DEFAULT_STRATEGY_NAME
    # The strategy objects don't have any hiphens ("utf-8" is written as "utf8")
    return getattr(TextEncodingStrategies, strategy_name)
