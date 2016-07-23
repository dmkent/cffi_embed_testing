class MyModel(object):
    def __init__(self):
        self.state_a = 0.0
        self.state_b = 1.0
        self.param1 = 1.5
        self.param2 = 1.0

    def run_step(self):
        self.state_b = self.param1 * self.state_a + self.param2

    def get_var_names(self):
        return ['state_a', 'state_b', 'param1', 'param2']

    def set_var(self, name, val):
        setattr(self, name, val)

    def get_var(self, name):
        return getattr(self, name)
