# Stubs for numpy.distutils.command.build_scripts (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from distutils.command.build_scripts import build_scripts as old_build_scripts

class build_scripts(old_build_scripts):
    def generate_scripts(self, scripts): ...
    scripts = ...  # type: Any
    def run(self): ...
    def get_source_files(self): ...