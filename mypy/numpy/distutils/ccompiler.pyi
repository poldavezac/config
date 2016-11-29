# Stubs for numpy.distutils.ccompiler (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from distutils.ccompiler import *

def replace_method(klass, method_name, func): ...
def CCompiler_spawn(self, cmd, display: Optional[Any] = ...): ...
def CCompiler_object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...
def CCompiler_compile(self, sources, output_dir: Optional[Any] = ..., macros: Optional[Any] = ..., include_dirs: Optional[Any] = ..., debug: int = ..., extra_preargs: Optional[Any] = ..., extra_postargs: Optional[Any] = ..., depends: Optional[Any] = ...): ...
def CCompiler_customize_cmd(self, cmd, ignore: Any = ...): ...
def CCompiler_show_customization(self): ...
def CCompiler_customize(self, dist, need_cxx: int = ...): ...
def simple_version_match(pat: str = ..., ignore: str = ..., start: str = ...): ...
def CCompiler_get_version(self, force: bool = ..., ok_status: Any = ...): ...
def CCompiler_cxx_compiler(self): ...
def new_compiler(plat: Optional[Any] = ..., compiler: Optional[Any] = ..., verbose: int = ..., dry_run: int = ..., force: int = ...): ...
def gen_lib_options(compiler, library_dirs, runtime_library_dirs, libraries): ...
def gen_preprocess_options(macros, include_dirs): ...
def split_quoted(s): ...