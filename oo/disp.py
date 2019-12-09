import psutil
for p in psutil.process_iter():
    try:
        path = p.exe()
    except psutil.AccessDenied:
        path = None
    p_dict = p.as_dict()
    proc = {
        "process_name": p_dict['name'],
        "process_id": p.pid,
        "path_file": path,
        'memory': p_dict['memory_percent']
    }
    print(proc)
