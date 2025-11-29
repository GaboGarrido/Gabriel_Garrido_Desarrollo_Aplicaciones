import runpy, traceback
try:
    g = runpy.run_path('mi_app/views.py')
    keys = [k for k in g.keys() if not k.startswith('__')]
    print('EXEC_KEYS:', keys)
    print('lista_actividades in exec ->', 'lista_actividades' in g)
except Exception:
    traceback.print_exc()
