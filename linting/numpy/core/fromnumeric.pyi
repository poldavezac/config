# Stubs for numpy.core.fromnumeric (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import multiarray as mu
from . import umath as um
from . import numerictypes as nt

def take(a, indices, axis: Optional[Any] = ..., out: Optional[Any] = ..., mode: str = ...): ...
def reshape(a, newshape, order: str = ...): ...
def choose(a, choices, out: Optional[Any] = ..., mode: str = ...): ...
def repeat(a, repeats, axis: Optional[Any] = ...): ...
def put(a, ind, v, mode: str = ...): ...
def swapaxes(a, axis1, axis2): ...
def transpose(a, axes: Optional[Any] = ...): ...
def partition(a, kth, axis: int = ..., kind: str = ..., order: Optional[Any] = ...): ...
def argpartition(a, kth, axis: int = ..., kind: str = ..., order: Optional[Any] = ...): ...
def sort(a, axis: int = ..., kind: str = ..., order: Optional[Any] = ...): ...
def argsort(a, axis: int = ..., kind: str = ..., order: Optional[Any] = ...): ...
def argmax(a, axis: Optional[Any] = ..., out: Optional[Any] = ...): ...
def argmin(a, axis: Optional[Any] = ..., out: Optional[Any] = ...): ...
def searchsorted(a, v, side: str = ..., sorter: Optional[Any] = ...): ...
def resize(a, new_shape): ...
def squeeze(a, axis: Optional[Any] = ...): ...
def diagonal(a, offset: int = ..., axis1: int = ..., axis2: int = ...): ...
def trace(a, offset: int = ..., axis1: int = ..., axis2: int = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
def ravel(a, order: str = ...): ...
def nonzero(a): ...
def shape(a): ...
def compress(condition, a, axis: Optional[Any] = ..., out: Optional[Any] = ...): ...
def clip(a, a_min, a_max, out: Optional[Any] = ...): ...
def sum(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def product(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def sometrue(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def alltrue(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def any(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def all(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def cumsum(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
def cumproduct(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
def ptp(a, axis: Optional[Any] = ..., out: Optional[Any] = ...): ...
def amax(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def amin(a, axis: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def alen(a): ...
def prod(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def cumprod(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
def ndim(a): ...
def rank(a): ...
def size(a, axis: Optional[Any] = ...): ...
def around(a, decimals: int = ..., out: Optional[Any] = ...): ...
def round_(a, decimals: int = ..., out: Optional[Any] = ...): ...
def mean(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., keepdims: Any = ...): ...
def std(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., ddof: int = ..., keepdims: Any = ...): ...
def var(a, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ..., ddof: int = ..., keepdims: Any = ...): ...
