import wmi

def detect_active_tf2()->bool:

    f = wmi.WMI()
    print("pid      Process Name")
    for process in f.Win32_Process():
        if process.Name == 'hl2.exe':
            return True
    return False
