# 6. Modules
https://docs.python.org/3/tutorial/modules.html

## Modules
This does not add the names of the functions defined in fibo directly to the current
namespace (see Python Scopes and Namespaces for more details); it only adds the module
name fibo there. Using the module name you can access the functions:
```python
import katas.fibonacci
katas.fibonacci.fib2(125)

from katas.fibonacci import fib
fib(500)

from katas.fibonacci import *

import katas.fibonacci as fib

from katas import fibonacci as fibo
```
# Packages
Packages are a way of structuring Python’s module namespace by using “dotted module names”.
For example, the module name A.B designates a submodule named B in a package named A.
```python
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
```
## Intra-package references
When packages are structured into subpackages (as with the sound package in the example),
you can use absolute imports to refer to submodules of siblings packages. For example, if the module
sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use from
sound.effects import echo.

You can also write relative imports, with the from module import name form of import statement.
These imports use leading dots to indicate the current and parent packages involved in the relative
import. From the surround module for example, you might use:
```python
from . import echo
from .. import formats
from ..filters import equalizer
```
Note that relative imports are based on the name of the current module. Since the name of the main
module is always "__main__", modules intended for use as the main module of a Python application
must always use absolute imports.