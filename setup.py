from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
from Cython.Compiler.Options import get_directive_defaults
directive_defaults = get_directive_defaults()
directive_defaults['linetrace'] = True
directive_defaults['binding'] = True

ext_options = dict(
    define_macros=[("CYTHON_TRACE_NOGIL", "1")])

setup(
    ext_modules=cythonize([
        Extension('tryfinally.test', ['tryfinally/test.pyx'], **ext_options),
        Extension('tryfinally.test2', ['tryfinally/test2.pyx'], **ext_options)]
    )
)
