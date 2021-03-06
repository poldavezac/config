# Stubs for numpy.distutils.fcompiler.compaq (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from numpy.distutils.fcompiler import FCompiler

compilers = ...  # type: Any

class CompaqFCompiler(FCompiler):
    compiler_type = ...  # type: str
    description = ...  # type: str
    version_pattern = ...  # type: str
    fc_exe = ...  # type: str
    executables = ...  # type: Any
    module_dir_switch = ...  # type: str
    module_include_switch = ...  # type: str
    def get_flags(self): ...
    def get_flags_debug(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_linker_so(self): ...

class CompaqVisualFCompiler(FCompiler):
    compiler_type = ...  # type: str
    description = ...  # type: str
    version_pattern = ...  # type: str
    compile_switch = ...  # type: str
    object_switch = ...  # type: str
    library_switch = ...  # type: str
    static_lib_extension = ...  # type: str
    static_lib_format = ...  # type: str
    module_dir_switch = ...  # type: str
    module_include_switch = ...  # type: str
    ar_exe = ...  # type: str
    fc_exe = ...  # type: str
    m = ...  # type: Any
    msg = ...  # type: Any
    e = ...  # type: Any
    executables = ...  # type: Any
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_debug(self): ...
