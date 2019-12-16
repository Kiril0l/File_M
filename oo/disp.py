import psutil
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


for p in psutil.process_iter():
    try:
        path = p.exe()
    except psutil.AccessDenied:
        path = None
    p_dict = p.as_dict()
    proc = [{
        "proc_name": p_dict['name'],
        "pid": p.pid,
        "gg": path,
        "HH": p_dict['memory_percent']
    }]
    print(proc)

proc_list = Gtk.ListStore(str, int, str, float)
for item in proc:
    proc_list.append(list(item))
for row in proc_list:
    print(row[:])
