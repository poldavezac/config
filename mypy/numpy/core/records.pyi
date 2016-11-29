# Stubs for numpy.core.records (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import numeric as sb
from . import numerictypes as nt
from .multiarray import ndarray

class format_parser:
    dtype = ...  # type: Any
    def __init__(self, formats, names, titles, aligned: bool = ..., byteorder: Optional[Any] = ...) -> None: ...

class record(nt.void):
    __name__ = ...  # type: str
    __module__ = ...  # type: str
    def __getattribute__(self, attr): ...
    def __setattr__(self, attr, val): ...
    def __getitem__(self, indx): ...
    def pprint(self): ...

class recarray(ndarray):
    __name__ = ...  # type: str
    __module__ = ...  # type: str
    def __new__(subtype, shape, dtype: Optional[Any] = ..., buf: Optional[Any] = ..., offset: int = ..., strides: Optional[Any] = ..., formats: Optional[Any] = ..., names: Optional[Any] = ..., titles: Optional[Any] = ..., byteorder: Optional[Any] = ..., aligned: bool = ..., order: str = ...): ...
    dtype = ...  # type: Any
    def __array_finalize__(self, obj): ...
    def __getattribute__(self, attr): ...
    def __setattr__(self, attr, val): ...
    def __getitem__(self, indx): ...
    def field(self, attr, val: Optional[Any] = ...): ...