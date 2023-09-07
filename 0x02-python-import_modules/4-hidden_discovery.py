""" import imp
from inspect import getmembers, isfunction
h = imp.load_compiled("hidden", "hidden_4.pyc")
#help(hidden_module)
#print(h.__all__)
#print(dir(h))
#print(a for a in getmembers(h) if isfunction(a[1]))
for func in dir(h):
    print(func) """
import importlib.util
from inspect import getmembers, isfunction
# Define the module name and path
module_name = "hidden"
module_path = "hidden_4.pyc"
# Load the compiled module
spec = importlib.util.spec_from_file_location(module_name, module_path)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
for name, obj in getmembers(h):
    if isfunction(obj) and name != "__init__":
        print(name)
