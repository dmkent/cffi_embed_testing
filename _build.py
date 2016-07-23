import cffi

ffibuilder = cffi.FFI()

header = 'include/my_model.h'

with open(header) as fobj:
    ffibuilder.embedding_api(fobj.read())

ffibuilder.set_source("my_model", "")

ffibuilder.embedding_init_code("""
    import weakref

    from my_model import ffi
    from mypackage.python_class import MyModel

    # These are used to make sure we don't get our objects garbage collected
    global_weakkeydict = weakref.WeakKeyDictionary()
    global_models = []

    @ffi.def_extern()
    def create_model():
        model = ffi.new_handle(MyModel())
        global_models.insert(-1, model)
        return model

    @ffi.def_extern()
    def destroy_model(model):
        global_models.remove(model)

    @ffi.def_extern()
    def model_run_step(model):
        ffi.from_handle(model).run_step()

    @ffi.def_extern()
    def model_get_var_names(model, size):
        model_obj = ffi.from_handle(model)
        vars = model_obj.get_var_names()
        cvars_list = [ffi.new('char[]', bytes(var, 'utf-8')) for var in vars]
        cvars = ffi.new('char*[]', cvars_list)
        # The items in the list will get garbage collected if we don't keep a
        # reference to them
        global_weakkeydict[cvars] = cvars_list
        size[0] = len(vars)
        return cvars

    @ffi.def_extern()
    def model_get_var(model, name):
        return ffi.from_handle(model).get_var(ffi.string(name).decode("utf-8"))

    @ffi.def_extern()
    def model_set_var(model, name, value):
        ffi.from_handle(model).set_var(ffi.string(name).decode('utf-8'), value)
""")

ffibuilder.compile(target="plugin.*", verbose=True)
