# https://docs.python.org/3/tutorial/modules.html

# Modules
# This does not add the names of the functions defined in fibo directly to the current
# namespace (see Python Scopes and Namespaces for more details); it only adds the module
# name fibo there. Using the module name you can access the functions:
import fibo
fibo.fib2(125)

from fibo import fib
fib(500)

from fibo import *

import fibo as fib

from fibo import fib as fibonacci

# Packages
# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
# For example, the module name A.B designates a submodule named B in a package named A.
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

import sound.effects.echo # Import the package
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects import echo # Import the module
echo.echofilter(input, output, delay=0.7, atten=4)

# Intra-package references
