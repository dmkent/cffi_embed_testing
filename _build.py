import os

import cffi

ffibuilder = cffi.FFI()

src_path = os.path.dirname(__file__)
header = os.path.join(src_path, 'include', 'my_model.h')
frozen_py_code = os.path.join(src_path, 'frozen.py')

with open(header) as fobj:
    ffibuilder.embedding_api(fobj.read())

ffibuilder.set_source("my_model", "", extra_link_args=['-Wl,-soname,my_model.so'])

with open(frozen_py_code) as fobj:
    ffibuilder.embedding_init_code(fobj.read())

ffibuilder.compile(verbose=True)
