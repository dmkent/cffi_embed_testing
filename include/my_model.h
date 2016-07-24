extern void * create_model(const char* classname);

extern void destroy_model(void* model);
    
extern void model_run_step(void *model);

extern char ** model_get_var_names(void *model, int* size);

extern double model_get_var(void *model, const char *name);

extern void model_set_var(void *model, const char *name, double value);
