import cffi

ffibuilder = cffi.FFI()

header = 'include/my_model.h'
frozen_py_code = 'frozen.py'

with open(header) as fobj:
    ffibuilder.embedding_api(fobj.read())

ffibuilder.set_source("my_model", "")

with open(frozen_py_code) as fobj:
    ffibuilder.embedding_init_code(fobj.read())

ffibuilder.compile(target="plugin.*", verbose=True)
