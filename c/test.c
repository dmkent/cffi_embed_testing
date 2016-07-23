#include <stdio.h>
#include "my_model.h"

int main(int argc, char* argv[]){
    /* create model */
    void * model_handle = create_model();

    /* find out the varible names */
    int i, nvars = 0;
    char ** var_names;
    var_names = model_get_var_names(model_handle, &nvars);
    printf("Vars are:%d\n", nvars);
    for (i=0; i < nvars; i++){
        printf("    %s\n", var_names[i]);
    }
    /* set some values */
    model_set_var(model_handle, "param1", 2.0);
    model_set_var(model_handle, "param2", 0.5);

    /* print current state */
    printf("a: %f\n", model_get_var(model_handle, "state_a"));
    printf("b: %f\n", model_get_var(model_handle, "state_b"));

    /* move forward one step */
    model_run_step(model_handle);

    /* print current state */
    printf("a: %f\n", model_get_var(model_handle, "state_a"));
    printf("b: %f\n", model_get_var(model_handle, "state_b"));

    destroy_model(model_handle);

}
