#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
extern "C" {

#include "my_model.h"
}

class MyModel
{
    public:
    MyModel()
    {
        _model = create_model();
    }

    ~MyModel()
    {
        destroy_model(_model);
    }

    std::vector<std::string> GetVariableNames(){
        int lencvars=0;
        char** cvars = model_get_var_names(_model, &lencvars);
        std::vector<std::string> vars(cvars, cvars + lencvars);
        return vars;
    }

    double GetVariable(std::string varName){
        return model_get_var(_model, varName.c_str());
    }

    void SetVariable(std::string varName, double value){
        model_set_var(_model, varName.c_str(), value);
    }

    void RunStep(){
        model_run_step(_model);
    }
    private:
    void *_model;
};

int main(int argc, char* argv[]){
    /* create model */
    MyModel *model = new MyModel();

    /* find out the varible names */
    std::vector<std::string> varnames = model->GetVariableNames();
    for(auto const &vname: varnames){
        std::cout << "  " << vname << "\n";
    }
    /* set some values */
    model->SetVariable("param1", 2.0);
    model->SetVariable("param2", 0.5);

    /* print current state */
    std::cout << "a: " << model->GetVariable("state_a") << "\n";
    std::cout << "b: " << model->GetVariable("state_b") << "\n";

    /* move forward one step */
    model->RunStep();

    /* print current state */
    std::cout << "a: " << model->GetVariable("state_a") << "\n";
    std::cout << "b: " << model->GetVariable("state_b") << "\n";

    delete model;
}
