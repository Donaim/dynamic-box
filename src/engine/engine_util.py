
import os, sys
import inspect
import importlib.util

def get_module_name(path: str):
    bname = os.path.basename(path)
    split = os.path.splitext(bname)
    return split[0]

def load_dynamic(path: str):
    module_name = get_module_name(path)
    spec = importlib.util.spec_from_file_location(module_name, path)

    re = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(re)

    return re

def get_last_class_from_module(mod):
    mems = inspect.getmembers(mod)
    for name, obj in reversed(mems):
        if (inspect.isclass(obj)):
            return obj

    return None

