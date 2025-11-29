import importlib, traceback
try:
    m = importlib.import_module('mi_app.models')
    print('MODULE:', m)
    print('FILE:', getattr(m, '__file__', 'NOFILE'))
    print('ATTRS:', [x for x in dir(m) if not x.startswith('__')])
    print('HAS Actividad ->', hasattr(m, 'Actividad'))
except Exception:
    traceback.print_exc()
