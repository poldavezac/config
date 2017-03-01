# Stubs for numpy.distutils.fcompiler.mips (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from numpy.distutils.fcompiler import FCompiler

compilers = ...  # type: Any

class MIPSFCompiler(FCompiler):
    compiler_type = ...  # type: str
    description = ...  # type: str
    version_pattern = ...  # type: str
    executables = ...  # type: Any
    module_dir_switch = ...  # type: Any
    module_include_switch = ...  # type: Any
    pic_flags = ...  # type: Any
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_arch_f77(self): ...
    def get_flags_arch_f90(self): ...