"""Loads play/.k4_3_lib.py (a dotfile, so not importable by name) as module `lib`."""
import importlib.util, os
_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".k4_3_lib.py")
_s = importlib.util.spec_from_file_location("k4_3_lib", _p)
lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(lib)
