# CFFI Embedding Demo

Attempts to demonstrate embedding a Python implementation of a time-series 
model into C or C++ code using CFFI.

The model to be embedded is in `lib/my_package/python_class.py`.

The main embedding CFFI code is then in `_build.py`. This builds a
.so file when run.

There are C and C++ command line programs that then use the exported interface 
from `include/my_model.h` to access and use the embedded Python code.

## Using

To build and run this try:

```bash
export PATH=~/miniconda3/bin:$PATH
conda env create -f cffi_env.yaml
source activate cffi

mkdir cmakebuild
cd cmakebuild/
cmake -DCMAKE_INSTALL_PREFIX=install .. && make install
PYTHONPATH=../lib LD_LIBRARY_PATH=install/lib ./install/bin/test
PYTHONPATH=../lib LD_LIBRARY_PATH=install/lib ./install/bin/testcpp
```

## Todo

* Test on windows
