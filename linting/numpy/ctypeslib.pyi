# Stubs for numpy.ctypeslib (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from numpy import dtype as _dtype
from numpy import intp as c_intp

ctypes_load_library = ...  # type: Any
load_library = ...  # type: Any
as_ctypes = ...  # type: Any
as_array = ...  # type: Any
c_intp = ...  # type: Any

class _ndptr(_ndptr_base):
    @property
    def __array_interface__(self): ...
    @classmethod
    def from_param(cls, obj): ...

def ndpointer(dtype: Optional[Any] = ..., ndim: Optional[Any] = ..., shape: Optional[Any] = ..., flags: Optional[Any] = ...): ...

# Names in __all__ with no definition:
#   test
