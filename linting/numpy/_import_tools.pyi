# Stubs for numpy._import_tools (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PackageLoader:
    parent_frame = ...  # type: Any
    parent_name = ...  # type: Any
    parent_path = ...  # type: Any
    parent_export_names = ...  # type: Any
    info_modules = ...  # type: Any
    imported_packages = ...  # type: Any
    verbose = ...  # type: Any
    def __init__(self, verbose: bool = ..., infunc: bool = ...) -> None: ...
    def __call__(self, *packages, **options): ...
    def log(self, mess): ...
    def warn(self, mess): ...
    def error(self, mess): ...
    def get_pkgdocs(self): ...

class PackageLoaderDebug(PackageLoader): ...