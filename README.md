# CFFI Embedding Demo

Attempts to demonstrate embedding a Python implementation of a time-series 
model into C or C++ code using CFFI.

The model to be embedded is in `lib/my_package/python_class.py`.

The main embedding CFFI code is then in `_build.py`. This builds a
.so file when run.

There are C and C++ command line programs that then use the exported interface 
from `include/my_model.h` to access and use the embedded Python code.


`build.sh` gives steps to build and run demos.
