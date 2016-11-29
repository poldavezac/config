# Stubs for numpy.core.arrayprint (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import numerictypes as _nt

def set_printoptions(precision: Optional[Any] = ..., threshold: Optional[Any] = ..., edgeitems: Optional[Any] = ..., linewidth: Optional[Any] = ..., suppress: Optional[Any] = ..., nanstr: Optional[Any] = ..., infstr: Optional[Any] = ..., formatter: Optional[Any] = ...): ...
def get_printoptions(): ...
def array2string(a, max_line_width: Optional[Any] = ..., precision: Optional[Any] = ..., suppress_small: Optional[Any] = ..., separator: str = ..., prefix: str = ..., style: Any = ..., formatter: Optional[Any] = ...): ...

class FloatFormat:
    precision = ...  # type: Any
    suppress_small = ...  # type: Any
    sign = ...  # type: Any
    exp_format = ...  # type: bool
    large_exponent = ...  # type: bool
    max_str_len = ...  # type: int
    def __init__(self, data, precision, suppress_small, sign: bool = ...) -> None: ...
    special_fmt = ...  # type: Any
    format = ...  # type: Any
    def fillFormat(self, data): ...
    def __call__(self, x, strip_zeros: bool = ...): ...

class IntegerFormat:
    format = ...  # type: Any
    def __init__(self, data) -> None: ...
    def __call__(self, x): ...

class LongFloatFormat:
    precision = ...  # type: Any
    sign = ...  # type: Any
    def __init__(self, precision, sign: bool = ...) -> None: ...
    def __call__(self, x): ...

class LongComplexFormat:
    real_format = ...  # type: Any
    imag_format = ...  # type: Any
    def __init__(self, precision) -> None: ...
    def __call__(self, x): ...

class ComplexFormat:
    real_format = ...  # type: Any
    imag_format = ...  # type: Any
    def __init__(self, x, precision, suppress_small) -> None: ...
    def __call__(self, x): ...

class DatetimeFormat:
    timezone = ...  # type: Any
    unit = ...  # type: Any
    casting = ...  # type: Any
    def __init__(self, x, unit: Optional[Any] = ..., timezone: Optional[Any] = ..., casting: str = ...) -> None: ...
    def __call__(self, x): ...

class TimedeltaFormat:
    format = ...  # type: Any
    def __init__(self, data) -> None: ...
    def __call__(self, x): ...