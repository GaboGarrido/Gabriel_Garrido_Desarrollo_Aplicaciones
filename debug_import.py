import importlib, traceback

try:
    m = importlib.import_module('mi_app.views')
    attrs = [x for x in dir(m) if not x.startswith('__')]
    print('MODULE:', m)
    try:
        print('FILE:', m.__file__)
    except Exception:
        print('MODULE has no __file__')
    print('ATTRS:', attrs)
    print('HAS lista_actividades ->', hasattr(m, 'lista_actividades'))
except Exception:
    traceback.print_exc()
